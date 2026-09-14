(function () {
  'use strict';

  /* ---------------- THEME TOGGLE ---------------- */
  (function () {
    var t = document.querySelector('[data-theme-toggle]'), r = document.documentElement;
    var d = matchMedia('(prefers-color-scheme:dark)').matches ? 'dark' : 'light';
    function paint() {
      r.setAttribute('data-theme', d);
      t.setAttribute('aria-label', 'Alternar para modo ' + (d === 'dark' ? 'claro' : 'escuro'));
      t.innerHTML = d === 'dark'
        ? '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>'
        : '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
    }
    paint();
    t.addEventListener('click', function () { d = d === 'dark' ? 'light' : 'dark'; paint(); });
  })();

  /* ---------------- DATA ---------------- */
  var DATA = window.CPA_DATA;
  var MCQ = DATA.mcq.map(function (q, i) { return Object.assign({}, q, { type: 'mcq', id: 'm' + i, num: i + 1 }); });
  var TREES = DATA.trees.map(function (q, i) { return Object.assign({}, q, { type: 'tree', id: 't' + i, num: MCQ.length + i + 1 }); });
  var QUESTIONS = MCQ.concat(TREES);
  var TOTAL = QUESTIONS.length;

  var THEME_ORDER = [
    'Sistema Financeiro Nacional',
    'Produtos do mercado financeiro',
    'Relacionamento com o cliente',
    'Inovação e desenvolvimento de mercado',
  ];
  var THEME_SHORT = {
    'Sistema Financeiro Nacional': 'SFN',
    'Produtos do mercado financeiro': 'Produtos',
    'Relacionamento com o cliente': 'Relacionamento',
    'Inovação e desenvolvimento de mercado': 'Inovação',
  };

  /* ---------------- STATE ---------------- */
  var state = {
    screen: 'start',
    current: 0,
    mcqAnswers: {},      // id -> selected option index
    treeAnswers: {},     // id -> array of selected option index per step (null = unanswered)
    treePointer: {},     // id -> which step is currently displayed
    flags: {},           // id -> bool
    timeLeftSec: DATA.meta.duration_minutes * 60,
    timerHandle: null,
    startedAt: null,
    finishedAt: null,
    reviewFilter: 'all', // all | wrong | theme name
  };

  QUESTIONS.forEach(function (q) {
    if (q.type === 'tree') {
      state.treeAnswers[q.id] = new Array(q.steps.length).fill(null);
      state.treePointer[q.id] = 0;
    }
  });

  var app = document.getElementById('app');

  function esc(s) { return String(s); }

  /* ================= START SCREEN ================= */
  function renderStart() {
    var weights = DATA.meta.weights;
    var barsHtml = THEME_ORDER.map(function (theme) {
      var pct = weights[theme];
      var mc = DATA.meta.mcq_counts[theme] || 0;
      var tc = DATA.meta.tree_counts[theme] || 0;
      return '' +
        '<div class="theme-bar">' +
          '<span class="theme-bar__label">' + theme + '</span>' +
          '<span class="theme-bar__pct">' + pct + '% · ' + mc + ' ME + ' + tc + ' AD</span>' +
          '<div class="theme-bar__track"><div class="theme-bar__fill" style="width:' + pct + '%"></div></div>' +
        '</div>';
    }).join('');

    app.innerHTML = '' +
      '<section class="hero">' +
        '<div>' +
          '<div class="hero__eyebrow">Simulado · Formato oficial 2026</div>' +
          '<h1>' + DATA.meta.title + '</h1>' +
          '<p class="hero__sub">' + DATA.meta.subtitle + ' — reproduzindo a estrutura divulgada pela ANBIMA para a nova certificação CPA (Certificado Profissional ANBIMA), que substitui a CPA-10 a partir de janeiro de 2026.</p>' +
        '</div>' +
        '<div class="stat-grid">' +
          '<div class="stat-card"><strong>' + DATA.meta.total_questions + '</strong><span>questões (40 múltipla escolha + 10 árvore de decisão)</span></div>' +
          '<div class="stat-card"><strong>2h30</strong><span>duração total da prova</span></div>' +
          '<div class="stat-card"><strong>' + DATA.meta.passing_pct + '%</strong><span>mínimo para aprovação (' + DATA.meta.passing_correct + ' acertos)</span></div>' +
          '<div class="stat-card"><strong>4</strong><span>módulos do programa detalhado</span></div>' +
        '</div>' +
      '</section>' +

      '<div class="card">' +
        '<h2>Distribuição por módulo do programa detalhado</h2>' +
        '<div class="theme-bars">' + barsHtml + '</div>' +
      '</div>' +

      '<div class="card">' +
        '<h2>Como funciona</h2>' +
        '<ul class="rules-list">' +
          li('São 40 questões de múltipla escolha contextualizadas (situações práticas de atendimento e mercado) e 10 questões interativas em formato de árvore de decisão, com 3 etapas encadeadas cada.') +
          li('O cronômetro de 2h30 começa a contar assim que você iniciar e é regressivo, exatamente como no exame real — o simulado é enviado automaticamente ao fim do tempo.') +
          li('Nas questões interativas, cada escolha revela uma consequência imediata antes de avançar para a próxima etapa da situação — simulando o atendimento real ao cliente.') +
          li('Você pode navegar livremente entre as questões, marcar para revisão e alterar respostas de múltipla escolha até finalizar o simulado.') +
          li('Ao final, você recebe a nota, o resultado (aprovado/reprovado a partir de 70%), o desempenho por módulo e o gabarito comentado de todas as 50 questões.') +
        '</ul>' +
        '<div class="cta-row">' +
          '<button class="btn" id="start-btn">Iniciar simulado</button>' +
          '<span class="q-index">Tempo estimado: 2h30 · você pode finalizar antes se concluir todas as questões</span>' +
        '</div>' +
      '</div>';

    document.getElementById('start-btn').addEventListener('click', startExam);
  }

  function li(text) {
    return '<li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="9"/></svg><span>' + text + '</span></li>';
  }

  /* ================= EXAM FLOW ================= */
  function startExam() {
    state.screen = 'exam';
    state.startedAt = Date.now();
    state.current = 0;
    document.getElementById('timer').hidden = false;
    startTimer();
    renderExam();
  }

  function startTimer() {
    updateTimerText();
    state.timerHandle = setInterval(function () {
      state.timeLeftSec--;
      updateTimerText();
      if (state.timeLeftSec <= 0) {
        clearInterval(state.timerHandle);
        submitExam();
      }
    }, 1000);
  }

  function updateTimerText() {
    var s = Math.max(0, state.timeLeftSec);
    var h = Math.floor(s / 3600);
    var m = Math.floor((s % 3600) / 60);
    var sec = s % 60;
    var text = h + ':' + String(m).padStart(2, '0') + ':' + String(sec).padStart(2, '0');
    var el = document.getElementById('timer-text');
    if (el) el.textContent = text;
    var timerBox = document.getElementById('timer');
    if (timerBox) {
      timerBox.classList.remove('timer--warning', 'timer--danger');
      if (s <= 300) timerBox.classList.add('timer--danger');
      else if (s <= 1800) timerBox.classList.add('timer--warning');
    }
  }

  function isAnswered(q) {
    if (q.type === 'mcq') return state.mcqAnswers[q.id] !== undefined;
    return state.treeAnswers[q.id].every(function (a) { return a !== null; });
  }

  function renderExam() {
    var q = QUESTIONS[state.current];
    var pct = Math.round(((state.current + 1) / TOTAL) * 100);

    app.innerHTML = '' +
      '<div class="progress-bar"><div class="progress-bar__fill" style="width:' + pct + '%"></div></div>' +
      '<div class="exam-layout">' +
        '<div>' +
          '<div class="q-meta">' +
            '<span class="tag' + (q.type === 'tree' ? ' tag--gold' : '') + '">' + (q.type === 'tree' ? 'Questão interativa · árvore de decisão' : 'Múltipla escolha contextualizada') + '</span>' +
            '<span class="tag">' + q.theme + '</span>' +
            '<span class="q-index">Questão ' + q.num + ' de ' + TOTAL + '</span>' +
          '</div>' +
          '<div class="q-card" id="q-card"></div>' +
          '<div class="exam-controls">' +
            '<div class="exam-controls-left">' +
              '<button class="btn btn--secondary btn--sm" id="prev-btn" ' + (state.current === 0 ? 'disabled' : '') + '>← Anterior</button>' +
              '<button class="flag-btn' + (state.flags[q.id] ? ' active' : '') + '" id="flag-btn">' + flagIcon() + (state.flags[q.id] ? 'Marcada' : 'Marcar p/ revisão') + '</button>' +
            '</div>' +
            '<div class="exam-controls-right">' +
              (state.current === TOTAL - 1
                ? '<button class="btn" id="finish-btn">Finalizar simulado</button>'
                : '<button class="btn btn--secondary btn--sm" id="next-btn">Próxima →</button>') +
            '</div>' +
          '</div>' +
        '</div>' +
        '<aside class="exam-nav">' +
          '<h3>Navegação</h3>' +
          '<div class="nav-legend">' +
            '<span><span class="legend-dot" style="background:var(--color-primary-highlight);border:1px solid var(--color-primary)"></span>Respondida</span>' +
            '<span><span class="legend-dot" style="background:var(--color-gold-highlight)"></span>Interativa</span>' +
            '<span><span class="legend-dot" style="border:1px solid var(--color-warning)"></span>Marcada</span>' +
          '</div>' +
          '<div class="nav-grid" id="nav-grid"></div>' +
          '<div style="margin-top:var(--space-5)"><button class="btn btn--outline btn--sm" id="finish-btn-side" style="width:100%">Finalizar simulado</button></div>' +
        '</aside>' +
      '</div>';

    renderNavGrid();
    renderQuestionBody(q);

    document.getElementById('prev-btn').addEventListener('click', function () { go(state.current - 1); });
    var nextBtn = document.getElementById('next-btn');
    if (nextBtn) nextBtn.addEventListener('click', function () { go(state.current + 1); });
    document.getElementById('flag-btn').addEventListener('click', function () {
      state.flags[q.id] = !state.flags[q.id];
      renderExam();
    });
    ['finish-btn', 'finish-btn-side'].forEach(function (id) {
      var btn = document.getElementById(id);
      if (btn) btn.addEventListener('click', confirmFinish);
    });
  }

  function flagIcon() {
    return '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right:4px;vertical-align:-2px"><path d="M4 21V4a1 1 0 0 1 1-1h13l-3 5 3 5H6a1 1 0 0 0-1 1v7"/></svg>';
  }

  function confirmFinish() {
    var answeredCount = QUESTIONS.filter(isAnswered).length;
    var msg = answeredCount < TOTAL
      ? 'Você respondeu ' + answeredCount + ' de ' + TOTAL + ' questões. Deseja finalizar o simulado mesmo assim?'
      : 'Finalizar o simulado e ver seu resultado?';
    if (window.confirm(msg)) submitExam();
  }

  function renderNavGrid() {
    var grid = document.getElementById('nav-grid');
    grid.innerHTML = QUESTIONS.map(function (q, i) {
      var cls = ['nav-cell'];
      if (q.type === 'tree') cls.push('tree-cell');
      if (i === state.current) cls.push('current');
      if (isAnswered(q)) cls.push('answered');
      if (state.flags[q.id]) cls.push('flagged');
      return '<button class="' + cls.join(' ') + '" data-i="' + i + '" title="Questão ' + q.num + '">' + q.num + '</button>';
    }).join('');
    grid.querySelectorAll('.nav-cell').forEach(function (btn) {
      btn.addEventListener('click', function () { go(parseInt(btn.dataset.i, 10)); });
    });
  }

  function go(i) {
    if (i < 0 || i >= TOTAL) return;
    state.current = i;
    renderExam();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  /* ---------------- QUESTION BODY: MCQ ---------------- */
  function renderQuestionBody(q) {
    var card = document.getElementById('q-card');
    if (q.type === 'mcq') {
      renderMcqBody(card, q);
    } else {
      renderTreeBody(card, q);
    }
  }

  function renderMcqBody(card, q) {
    var selected = state.mcqAnswers[q.id];
    card.innerHTML = '' +
      '<p class="q-context">' + q.context + '</p>' +
      '<div class="options">' + q.options.map(function (opt, idx) {
        var cls = 'option' + (selected === idx ? ' selected' : '');
        var letter = String.fromCharCode(65 + idx);
        return '<button class="' + cls + '" data-idx="' + idx + '"><span class="option__marker">' + letter + '</span><span>' + opt + '</span></button>';
      }).join('') + '</div>';

    card.querySelectorAll('.option').forEach(function (btn) {
      btn.addEventListener('click', function () {
        state.mcqAnswers[q.id] = parseInt(btn.dataset.idx, 10);
        renderExam();
      });
    });
  }

  /* ---------------- QUESTION BODY: DECISION TREE ---------------- */
  function renderTreeBody(card, q) {
    var answers = state.treeAnswers[q.id];
    var pointer = state.treePointer[q.id];
    var allDone = answers.every(function (a) { return a !== null; });

    var dots = q.steps.map(function (s, i) {
      var cls = 'tree-step-dot';
      if (answers[i] !== null) cls += ' done';
      else if (i === pointer) cls += ' active';
      return '<div class="' + cls + '"></div>';
    }).join('');

    var html = '' +
      '<div class="tree-scenario"><strong>' + q.title + '</strong>' + q.intro + '</div>' +
      '<div class="tree-steps">' + dots + '</div>';

    // render all answered steps as history, then the active step (if any)
    for (var i = 0; i < q.steps.length; i++) {
      var step = q.steps[i];
      var chosen = answers[i];
      if (chosen !== null) {
        html += renderStepBlock(q, i, step, chosen, true);
      } else if (i === pointer) {
        html += renderStepBlock(q, i, step, null, false);
        break;
      } else {
        break;
      }
    }

    if (allDone) {
      var correctSteps = answers.filter(function (a, i) { return q.steps[i].options[a].isBest; }).length;
      html += '<div class="feedback-box' + (correctSteps === q.steps.length ? ' is-correct' : '') + '" style="margin-top:var(--space-6)">' +
        '<strong>Cenário concluído</strong>Você acertou ' + correctSteps + ' de ' + q.steps.length + ' decisões nesta situação interativa. ' +
        (q.num < TOTAL ? 'Use "Próxima" para seguir ao simulado.' : 'Você pode finalizar o simulado agora.') +
        '</div>';
    }

    card.innerHTML = html;

    // wire up active step options
    var activeStepEl = card.querySelector('.js-active-step');
    if (activeStepEl) {
      var stepIdx = parseInt(activeStepEl.dataset.step, 10);
      activeStepEl.querySelectorAll('.option').forEach(function (btn) {
        btn.addEventListener('click', function () {
          var optIdx = parseInt(btn.dataset.idx, 10);
          state.treeAnswers[q.id][stepIdx] = optIdx;
          renderExam();
        });
      });
    }
    // wire up "continue" buttons on completed steps that are the latest answered one
    var contBtn = card.querySelector('.js-continue');
    if (contBtn) {
      contBtn.addEventListener('click', function () {
        state.treePointer[q.id] = parseInt(contBtn.dataset.next, 10);
        renderExam();
      });
    }
  }

  function renderStepBlock(q, idx, step, chosenIdx, isHistory) {
    var isActive = chosenIdx === null;
    var block = '<div class="' + (isActive ? 'js-active-step' : '') + '" ' + (isActive ? 'data-step="' + idx + '"' : '') + '>' +
      '<p class="tree-situation">' + step.situation + '</p>' +
      '<p class="q-context" style="font-weight:600">' + step.prompt + '</p>' +
      '<div class="options">' + step.options.map(function (opt, oi) {
        var cls = 'option';
        if (chosenIdx !== null) {
          cls += (oi === chosenIdx ? (opt.isBest ? ' correct' : ' incorrect') : '');
          if (oi !== chosenIdx && opt.isBest) cls += ' correct';
        }
        var letter = String.fromCharCode(65 + oi);
        var disabled = chosenIdx !== null ? 'disabled' : '';
        return '<button class="' + cls + '" data-idx="' + oi + '" ' + disabled + '><span class="option__marker">' + letter + '</span><span>' + opt.text + '</span></button>';
      }).join('') + '</div>';

    if (chosenIdx !== null) {
      var chosenOpt = step.options[chosenIdx];
      block += '<div class="feedback-box ' + (chosenOpt.isBest ? 'is-correct' : 'is-incorrect') + '">' +
        '<strong>' + (chosenOpt.isBest ? '✓ Melhor decisão' : '✗ Não é a melhor decisão') + '</strong>' + chosenOpt.feedback + '</div>';
      // show continue button only if this is the latest answered step (idx === pointer) and there's a next step
      if (idx === state.treePointer[q.id] && idx < q.steps.length - 1) {
        block += '<div style="margin-top:var(--space-4)"><button class="btn btn--sm js-continue" data-next="' + (idx + 1) + '">Continuar cenário →</button></div>';
      } else if (idx === state.treePointer[q.id] && idx === q.steps.length - 1) {
        // last step just answered — bump pointer so allDone logic renders summary next paint
        setTimeout(function () { state.treePointer[q.id] = q.steps.length; }, 0);
      }
    }
    block += '</div>';
    return block;
  }

  /* ================= SUBMIT / RESULTS ================= */
  function submitExam() {
    if (state.timerHandle) clearInterval(state.timerHandle);
    state.finishedAt = Date.now();
    state.screen = 'results';
    document.getElementById('timer').hidden = true;
    renderResults();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function scoreQuestion(q) {
    if (q.type === 'mcq') {
      var sel = state.mcqAnswers[q.id];
      return sel !== undefined && sel === q.correct ? 1 : 0;
    }
    var answers = state.treeAnswers[q.id];
    var correct = 0, total = q.steps.length;
    answers.forEach(function (a, i) {
      if (a !== null && q.steps[i].options[a].isBest) correct++;
    });
    return correct / total;
  }

  function renderResults() {
    var scores = QUESTIONS.map(scoreQuestion);
    var totalScore = scores.reduce(function (a, b) { return a + b; }, 0);
    var pct = (totalScore / TOTAL) * 100;
    var passed = pct >= DATA.meta.passing_pct;
    var roundedAcertos = Math.round(totalScore);

    var themeScores = {};
    THEME_ORDER.forEach(function (t) { themeScores[t] = { correct: 0, total: 0 }; });
    QUESTIONS.forEach(function (q, i) {
      themeScores[q.theme].correct += scores[i];
      themeScores[q.theme].total += 1;
    });

    var circumference = 2 * Math.PI * 80;
    var dash = (pct / 100) * circumference;

    var themeCardsHtml = THEME_ORDER.map(function (t) {
      var ts = themeScores[t];
      var tp = Math.round((ts.correct / ts.total) * 100);
      return '<div class="theme-result-card">' +
        '<div class="theme-result-card__top"><span>' + THEME_SHORT[t] + '</span><span>' + tp + '%</span></div>' +
        '<div class="theme-bar__track"><div class="theme-bar__fill" style="width:' + tp + '%"></div></div>' +
        '<p class="q-index" style="margin-top:6px">' + Math.round(ts.correct * 10) / 10 + ' de ' + ts.total + ' questões</p>' +
      '</div>';
    }).join('');

    var filterChips = ['all', 'wrong'].concat(THEME_ORDER);
    var chipLabels = { all: 'Todas', wrong: 'Somente erros' };
    var filterHtml = filterChips.map(function (f) {
      var label = chipLabels[f] || THEME_SHORT[f];
      return '<button class="filter-chip' + (state.reviewFilter === f ? ' active' : '') + '" data-f="' + f + '">' + label + '</button>';
    }).join('');

    app.innerHTML = '' +
      '<section class="result-hero">' +
        '<div class="result-ring">' +
          '<svg width="180" height="180" viewBox="0 0 180 180">' +
            '<circle cx="90" cy="90" r="80" fill="none" stroke="var(--color-surface-offset)" stroke-width="14"/>' +
            '<circle cx="90" cy="90" r="80" fill="none" stroke="' + (passed ? 'var(--color-success)' : 'var(--color-error)') + '" stroke-width="14" stroke-linecap="round" stroke-dasharray="' + dash + ' ' + circumference + '"/>' +
          '</svg>' +
          '<div class="result-ring__pct"><strong>' + pct.toFixed(1) + '%</strong><span>' + roundedAcertos + ' / ' + TOTAL + '</span></div>' +
        '</div>' +
        '<div class="result-status ' + (passed ? 'pass' : 'fail') + '">' + (passed ? 'Aprovado' : 'Reprovado') + '</div>' +
        '<p class="q-index">Mínimo exigido: ' + DATA.meta.passing_pct + '% (' + DATA.meta.passing_correct + ' acertos) · Tempo utilizado: ' + formatDuration(state) + '</p>' +
      '</section>' +

      '<div class="card">' +
        '<h2>Desempenho por módulo</h2>' +
        '<div class="theme-results">' + themeCardsHtml + '</div>' +
      '</div>' +

      '<div class="card">' +
        '<h2>Gabarito comentado</h2>' +
        '<div class="filter-row" id="filter-row">' + filterHtml + '</div>' +
        '<div id="review-list"></div>' +
      '</div>' +

      '<div class="cta-row" style="justify-content:center">' +
        '<button class="btn btn--secondary" id="restart-btn">Refazer simulado</button>' +
      '</div>';

    renderReviewList(scores);

    document.getElementById('filter-row').querySelectorAll('.filter-chip').forEach(function (chip) {
      chip.addEventListener('click', function () {
        state.reviewFilter = chip.dataset.f;
        renderResults();
      });
    });
    document.getElementById('restart-btn').addEventListener('click', restart);
  }

  function formatDuration() {
    var usedSec = DATA.meta.duration_minutes * 60 - state.timeLeftSec;
    var h = Math.floor(usedSec / 3600), m = Math.floor((usedSec % 3600) / 60);
    return h + 'h' + String(m).padStart(2, '0') + 'min';
  }

  function renderReviewList(scores) {
    var list = document.getElementById('review-list');
    var filtered = QUESTIONS.map(function (q, i) { return { q: q, score: scores[i] }; }).filter(function (item) {
      if (state.reviewFilter === 'all') return true;
      if (state.reviewFilter === 'wrong') return item.score < 1;
      return item.q.theme === state.reviewFilter;
    });

    list.innerHTML = filtered.map(function (item) { return renderReviewItem(item.q, item.score); }).join('') ||
      '<p class="q-index">Nenhuma questão nesse filtro.</p>';
  }

  function renderReviewItem(q, score) {
    var ok = score === 1;
    var badge = '<span class="review-badge ' + (ok ? 'ok' : 'no') + '">' + (ok ? '✓' : '✗') + '</span>';
    var head = '<div class="review-item__head">' + badge +
      '<span class="tag' + (q.type === 'tree' ? ' tag--gold' : '') + '">Questão ' + q.num + '</span>' +
      '<span class="tag">' + THEME_SHORT[q.theme] + '</span></div>';

    if (q.type === 'mcq') {
      var sel = state.mcqAnswers[q.id];
      var selText = sel !== undefined ? letterOpt(sel, q.options[sel]) : 'Não respondida';
      var correctText = letterOpt(q.correct, q.options[q.correct]);
      return '<div class="review-item">' + head +
        '<p class="review-item__context">' + q.context + '</p>' +
        '<div class="review-answer ' + (ok ? '' : 'your-wrong') + '">Sua resposta: ' + selText + '</div>' +
        (!ok ? '<div class="review-answer correct-answer">Gabarito: ' + correctText + '</div>' : '') +
        '<p class="review-explanation">' + q.explanation + '</p>' +
      '</div>';
    }

    var answers = state.treeAnswers[q.id];
    var stepsHtml = q.steps.map(function (step, i) {
      var chosen = answers[i];
      var chosenOpt = chosen !== null ? step.options[chosen] : null;
      var bestOpt = step.options.filter(function (o) { return o.isBest; })[0];
      return '<div style="margin:var(--space-3) 0;padding-left:var(--space-3);border-left:2px solid var(--color-divider)">' +
        '<p class="q-index" style="margin-bottom:4px">Etapa ' + (i + 1) + ' — ' + step.prompt + '</p>' +
        '<div class="review-answer ' + (chosenOpt && chosenOpt.isBest ? '' : 'your-wrong') + '">Sua escolha: ' + (chosenOpt ? chosenOpt.text : 'Não respondida') + '</div>' +
        (!chosenOpt || !chosenOpt.isBest ? '<div class="review-answer correct-answer">Melhor decisão: ' + bestOpt.text + '</div>' : '') +
        '<p class="review-explanation">' + (chosenOpt ? chosenOpt.feedback : bestOpt.feedback) + '</p>' +
      '</div>';
    }).join('');

    return '<div class="review-item">' + head +
      '<p class="review-item__context"><strong>' + q.title + '</strong> — ' + q.intro + '</p>' +
      stepsHtml +
      '<p class="q-index" style="margin-top:var(--space-2)">Pontuação nesta questão interativa: ' + Math.round(score * 100) + '%</p>' +
    '</div>';
  }

  function letterOpt(idx, text) {
    return String.fromCharCode(65 + idx) + ') ' + text;
  }

  function restart() {
    if (!window.confirm('Isso vai reiniciar o simulado do zero, apagando suas respostas atuais. Continuar?')) return;
    state.current = 0;
    state.mcqAnswers = {};
    state.treeAnswers = {};
    state.treePointer = {};
    state.flags = {};
    state.timeLeftSec = DATA.meta.duration_minutes * 60;
    state.reviewFilter = 'all';
    QUESTIONS.forEach(function (q) {
      if (q.type === 'tree') {
        state.treeAnswers[q.id] = new Array(q.steps.length).fill(null);
        state.treePointer[q.id] = 0;
      }
    });
    state.screen = 'start';
    renderStart();
    window.scrollTo({ top: 0 });
  }

  /* ---------------- INIT ---------------- */
  renderStart();
})();
