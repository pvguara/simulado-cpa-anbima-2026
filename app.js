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

  /* ---------------- DATA / RANDOM SAMPLING ---------------- */
  var POOL = window.CPA_POOL;

  var MCQ_SAMPLE_COUNTS = {
    'Sistema Financeiro Nacional': 10,
    'Produtos do mercado financeiro': 16,
    'Relacionamento com o cliente': 9,
    'Inovação e desenvolvimento de mercado': 5,
  };
  var TREE_SAMPLE_COUNTS = {
    'Produtos do mercado financeiro': 4,
    'Relacionamento com o cliente': 6,
  };

  function shuffleArr(arr) {
    var a = arr.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var tmp = a[i]; a[i] = a[j]; a[j] = tmp;
    }
    return a;
  }

  function sampleByTheme(pool, counts) {
    var result = [];
    Object.keys(counts).forEach(function (theme) {
      var group = pool.filter(function (x) { return x.theme === theme; });
      result = result.concat(shuffleArr(group).slice(0, counts[theme]));
    });
    return result;
  }

  function shuffleMcqOptions(q) {
    var order = shuffleArr(q.options.map(function (_, i) { return i; }));
    var newOptions = order.map(function (i) { return q.options[i]; });
    return Object.assign({}, q, { options: newOptions, correct: order.indexOf(q.correct) });
  }

  function shuffleTreeSteps(t) {
    var newSteps = t.steps.map(function (step) {
      return Object.assign({}, step, { options: shuffleArr(step.options) });
    });
    return Object.assign({}, t, { steps: newSteps });
  }

  function buildExamData() {
    var mcqSample = shuffleArr(sampleByTheme(POOL.mcq, MCQ_SAMPLE_COUNTS).map(shuffleMcqOptions));
    var treeSample = shuffleArr(sampleByTheme(POOL.trees, TREE_SAMPLE_COUNTS).map(shuffleTreeSteps));
    return { meta: POOL.meta, mcq: mcqSample, trees: treeSample };
  }

  var DATA, MCQ, TREES, QUESTIONS, TOTAL;

  function loadExam() {
    DATA = buildExamData();
    MCQ = DATA.mcq.map(function (q, i) { return Object.assign({}, q, { type: 'mcq', id: 'm' + i, num: i + 1 }); });
    TREES = DATA.trees.map(function (q, i) { return Object.assign({}, q, { type: 'tree', id: 't' + i, num: MCQ.length + i + 1 }); });
    QUESTIONS = MCQ.concat(TREES);
    TOTAL = QUESTIONS.length;

    state.current = 0;
    state.mcqAnswers = {};
    state.treeAnswers = {};
    state.treePointer = {};
    state.flags = {};
    state.timeLeftSec = state.durationMinutes * 60;
    state.notes = '';
    state.calcExpression = '';
    state.finishedAt = null;
    state.deadline = null;
    state.reviewFilter = 'all';

    QUESTIONS.forEach(function (q) {
      if (q.type === 'tree') {
        state.treeAnswers[q.id] = new Array(q.steps.length).fill(null);
        state.treePointer[q.id] = 0;
      }
    });
  }

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
    timeLeftSec: 0,
    timerHandle: null,
    startedAt: null,
    finishedAt: null,
    reviewFilter: 'all', // all | wrong | theme name
    mode: 'real',
    durationMinutes: 150,
    deadline: null,
    notes: '',
    calcExpression: '',
  };

  loadExam(); // draw the first random 40 MCQ + 10 árvore set from the pool

  var app = document.getElementById('app');

  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]; }); }

  var overlay = document.getElementById('app-dialog');
  var overlayReturnFocus;
  function closeDialog() {
    overlay.close();
    if (overlayReturnFocus && overlayReturnFocus.isConnected) overlayReturnFocus.focus();
  }
  function showDialog(title, html, wire) {
    if (overlay.open) overlay.close();
    overlayReturnFocus = document.activeElement;
    overlay.innerHTML = '<div class="dialog-heading"><h2 id="dialog-title">' + title + '</h2><button class="btn btn--secondary btn--sm" id="dialog-close">Fechar</button></div>' + html;
    overlay.querySelector('#dialog-close').addEventListener('click', closeDialog);
    overlay.showModal();
    if (wire) wire();
  }
  overlay.addEventListener('cancel', function (e) { e.preventDefault(); closeDialog(); });
  function ask(title, message, label, action) {
    showDialog(title, '<p>' + esc(message) + '</p><div class="cta-row"><button class="btn btn--secondary" id="dialog-cancel">Cancelar</button><button class="btn" id="dialog-confirm">' + label + '</button></div>', function () {
      overlay.querySelector('#dialog-cancel').addEventListener('click', closeDialog);
      overlay.querySelector('#dialog-confirm').addEventListener('click', function () {
        closeDialog();
        if (state.screen !== 'results' || title === 'Nova tentativa') action();
      });
      overlay.querySelector('#dialog-cancel').focus();
    });
  }

  /* ================= START SCREEN ================= */
  function renderStart() {
    var weights = DATA.meta.weights;
    var bankTotal = POOL.mcq.length + POOL.trees.length;
    var sourcesHtml = DATA.meta.sources.map(function (source) {
      return '<li><a href="' + esc(source.url) + '" target="_blank" rel="noopener noreferrer">' + esc(source.label) + '</a></li>';
    }).join('');
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
          '<div class="hero__eyebrow">Simulado independente · CPA 2026</div>' +
          '<h1>Simulado CPA · Certificação Profissional Anbima de Distribuição</h1>' +
          '<p class="hero__sub">Treine com 50 questões sorteadas de um banco de ' + bankTotal + ', cronômetro e gabarito comentado. Escolha entre navegação sequencial para treino de prova e navegação livre para estudo.</p>' +
          '<p class="q-index bank-summary">' + POOL.mcq.length + ' questões de múltipla escolha + ' + POOL.trees.length + ' árvores de diálogo no banco autoral.</p>' +
        '</div>' +
        '<div class="stat-grid">' +
          '<div class="stat-card"><strong>' + DATA.meta.total_questions + '</strong><span>questões (40 múltipla escolha + 10 árvores de diálogo)</span></div>' +
          '<div class="stat-card"><strong>2h30</strong><span>duração total da prova</span></div>' +
          '<div class="stat-card"><strong>' + DATA.meta.passing_pct + '%</strong><span>mínimo para aprovação (' + DATA.meta.passing_correct + ' acertos)</span></div>' +
          '<div class="stat-card"><strong>4</strong><span>módulos do programa detalhado</span></div>' +
        '</div>' +
      '</section>' +

      '<section class="card mode-settings" aria-labelledby="mode-title">' +
        '<h2 id="mode-title">Escolha como praticar</h2>' +
        '<fieldset class="mode-picker"><legend class="sr-only">Modo do simulado</legend>' +
          '<label class="mode-choice"><input type="radio" name="exam-mode" value="real" ' + (state.mode === 'real' ? 'checked' : '') + '><span><strong>Prova real</strong><span>Avance sem voltar. Questões anteriores ficam bloqueadas e o gabarito só aparece ao finalizar.</span></span></label>' +
          '<label class="mode-choice"><input type="radio" name="exam-mode" value="study" ' + (state.mode === 'study' ? 'checked' : '') + '><span><strong>Estudo</strong><span>Navegue livremente, marque para revisão e veja o feedback das árvores durante o treino.</span></span></label>' +
        '</fieldset>' +
        '<label class="extra-time"><input type="checkbox" id="extra-time" ' + (state.durationMinutes === 180 ? 'checked' : '') + '>Treinar com 30 minutos adicionais (total de 3h)</label>' +
        '<p class="q-index">Tempo padrão: 2h30. No exame oficial, tempo adicional depende de solicitação e aprovação das condições especiais; esta seleção apenas configura o treino.</p>' +
        '<p class="q-index">Referência: edital enviado, versão 1.6, setembro de 2026, itens 8.1 a 8.4. Esta interface não é uma reprodução da plataforma oficial.</p>' +
      '</section>' +

      '<div class="card">' +
        '<h2>Distribuição por módulo do programa detalhado</h2>' +
        '<div class="theme-bars">' + barsHtml + '</div>' +
      '</div>' +

      '<div class="card">' +
        '<h2>Como funciona</h2>' +
        '<ul class="rules-list">' +
          li('Cada tentativa sorteia 40 questões de múltipla escolha contextualizadas e 10 árvores de diálogo, com 3 etapas e 3 alternativas por etapa. As árvores são simplificações pedagógicas, não réplicas do modelo oficial. Não há um módulo separado de cases compartilhados.') +
          li('O banco tem questões autorais fáceis, médias e difíceis, com predominância intermediária. A dificuldade é uma estimativa pedagógica, sem calibração oficial ou garantia de equivalência com a prova.') +
          li('O cronômetro inicia ao começar a tentativa e o envio é automático ao acabar o tempo. Calculadora e bloco de notas estão disponíveis sem pausar o relógio.') +
          li('Em Prova real, ao avançar você bloqueia a questão anterior, mesmo em branco. Nas árvores, a correção fica oculta até o resultado. Em Estudo, continuam disponíveis navegação livre, marcação e feedback imediato.') +
          li('Ao final, você recebe a nota, o resultado (aprovado/reprovado a partir de 70%), o desempenho por módulo e o gabarito comentado de todas as 50 questões.') +
        '</ul>' +
        '<div class="cta-row">' +
          '<button class="btn" id="start-btn">Iniciar simulado</button>' +
          '<span class="q-index" id="start-summary">' + (state.durationMinutes === 180 ? '3h com tempo adicional' : '2h30') + ' · 50 questões por tentativa</span>' +
        '</div>' +
      '</div>' +

      '<section class="card references" aria-labelledby="references-title">' +
        '<h2 id="references-title">Modelos oficiais e referências</h2>' +
        '<p>O caderno público da ANBIMA reúne questões alinhadas ao exame-piloto. Ele serve como modelo de estilo e conteúdo, não como uma prova anterior completa. As questões deste simulado são autorais, sem reprodução de provas sigilosas.</p>' +
        '<p>Na ampliação, o programa detalhado orientou os temas; o caderno e o guia orientaram a construção de situações práticas, comandos e alternativas. Os novos itens identificam o tópico do programa no gabarito.</p>' +
        '<details><summary>Consultar materiais oficiais da ANBIMA</summary><ul class="reference-links">' + sourcesHtml + '</ul></details>' +
        '<p class="q-index">Materiais de apoio enviados nesta conversa não foram publicados nem incorporados como arquivos de download. Consulte sempre as versões e regras aplicáveis à data do seu exame.</p>' +
      '</section>';

    document.getElementById('start-btn').addEventListener('click', startExam);
    document.querySelectorAll('[name="exam-mode"]').forEach(function (input) {
      input.addEventListener('change', function () { state.mode = input.value; });
    });
    document.getElementById('extra-time').addEventListener('change', function (e) {
      state.durationMinutes = e.target.checked ? 180 : 150;
      document.getElementById('start-summary').textContent = (state.durationMinutes === 180 ? '3h com tempo adicional' : '2h30') + ' · 50 questões por tentativa';
    });
  }

  function li(text) {
    return '<li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="9"/></svg><span>' + text + '</span></li>';
  }

  /* ================= EXAM FLOW ================= */
  function startExam() {
    loadExam(); // sorteia um novo conjunto de 40 questões + 10 árvores do banco para esta tentativa
    state.screen = 'exam';
    state.startedAt = Date.now();
    state.deadline = state.startedAt + state.durationMinutes * 60000;
    document.getElementById('timer').hidden = false;
    startTimer();
    renderExam();
    window.scrollTo({ top: 0, behavior: 'instant' });
  }

  function startTimer() {
    if (state.timerHandle) clearInterval(state.timerHandle);
    updateTimerText();
    state.timerHandle = setInterval(function () {
      state.timeLeftSec = Math.max(0, Math.ceil((state.deadline - Date.now()) / 1000));
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
      '<div class="exam-toolbar"><span class="tag">' + (state.mode === 'real' ? 'Prova real · sem retorno' : 'Estudo · navegação livre') + '</span><div class="tool-buttons"><button class="btn btn--secondary btn--sm" id="calculator-btn">Calculadora</button><button class="btn btn--secondary btn--sm" id="notes-btn">Bloco de notas</button></div></div>' +
      (state.mode === 'real' ? '<p class="exam-notice">Ao avançar, a questão atual será bloqueada, mesmo se ficar em branco. O gabarito será exibido apenas após finalizar.</p>' : '') +
      '<div class="progress-bar"><div class="progress-bar__fill" style="width:' + pct + '%"></div></div>' +
      '<div class="exam-layout">' +
        '<div>' +
          '<div class="q-meta">' +
            '<span class="tag' + (q.type === 'tree' ? ' tag--gold' : '') + '">' + (q.type === 'tree' ? 'Questão interativa · árvore de diálogo' : 'Múltipla escolha contextualizada') + '</span>' +
            '<span class="tag">' + q.theme + '</span>' +
            '<span class="q-index">Questão ' + q.num + ' de ' + TOTAL + '</span>' +
          '</div>' +
          '<div class="q-card" id="q-card"></div>' +
          '<div class="exam-controls">' +
            '<div class="exam-controls-left">' +
              (state.mode === 'study' ? '<button class="btn btn--secondary btn--sm" id="prev-btn" ' + (state.current === 0 ? 'disabled' : '') + '>← Anterior</button>' +
              '<button class="flag-btn' + (state.flags[q.id] ? ' active' : '') + '" id="flag-btn">' + flagIcon() + (state.flags[q.id] ? 'Marcada' : 'Marcar p/ revisão') + '</button>' : '<span class="q-index">Questão ' + q.num + ' de ' + TOTAL + '</span>') +
            '</div>' +
            '<div class="exam-controls-right">' +
              (state.current === TOTAL - 1
                ? '<button class="btn" id="finish-btn">Finalizar simulado</button>'
                : '<button class="btn btn--secondary btn--sm" id="next-btn">Próxima →</button>') +
            '</div>' +
          '</div>' +
        '</div>' +
        '<aside class="exam-nav">' +
          '<h3>' + (state.mode === 'real' ? 'Progresso da tentativa' : 'Navegação') + '</h3>' +
          '<div class="nav-legend">' +
            '<span><span class="legend-dot" style="background:var(--color-primary-highlight);border:1px solid var(--color-primary)"></span>Respondida</span>' +
            '<span><span class="legend-dot" style="background:var(--color-gold-highlight)"></span>Interativa</span>' +
            (state.mode === 'study' ? '<span><span class="legend-dot" style="border:1px solid var(--color-warning)"></span>Marcada</span>' : '<span>Questões anteriores bloqueadas</span>') +
          '</div>' +
          '<div class="nav-grid" id="nav-grid"></div>' +
          '<div style="margin-top:var(--space-5)"><button class="btn btn--outline btn--sm" id="finish-btn-side" style="width:100%">Finalizar simulado</button></div>' +
        '</aside>' +
      '</div>';

    renderNavGrid();
    renderQuestionBody(q);

    document.getElementById('calculator-btn').addEventListener('click', openCalculator);
    document.getElementById('notes-btn').addEventListener('click', openNotes);
    var prevBtn = document.getElementById('prev-btn');
    if (prevBtn) prevBtn.addEventListener('click', function () { go(state.current - 1); });
    var nextBtn = document.getElementById('next-btn');
    if (nextBtn) nextBtn.addEventListener('click', function () { go(state.current + 1); });
    var flagBtn = document.getElementById('flag-btn');
    if (flagBtn) flagBtn.addEventListener('click', function () {
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
    ask('Finalizar tentativa', msg, 'Finalizar e ver resultado', submitExam);
  }

  function renderNavGrid() {
    var grid = document.getElementById('nav-grid');
    grid.innerHTML = QUESTIONS.map(function (q, i) {
      var cls = ['nav-cell'];
      if (q.type === 'tree') cls.push('tree-cell');
      if (i === state.current) cls.push('current');
      if (isAnswered(q)) cls.push('answered');
      if (state.flags[q.id]) cls.push('flagged');
      if (state.mode === 'real') {
        return '<span class="' + cls.join(' ') + (i < state.current ? ' locked' : '') + '" aria-label="Questão ' + q.num + (i < state.current ? ', bloqueada' : i === state.current ? ', atual' : ', não visualizada') + '"' + (i === state.current ? ' aria-current="step"' : '') + '>' + q.num + '</span>';
      }
      return '<button class="' + cls.join(' ') + '" data-i="' + i + '" title="Questão ' + q.num + '">' + q.num + '</button>';
    }).join('');
    grid.querySelectorAll('button.nav-cell').forEach(function (btn) {
      btn.addEventListener('click', function () { go(parseInt(btn.dataset.i, 10)); });
    });
  }

  function go(i) {
    if (state.screen !== 'exam' || i < 0 || i >= TOTAL) return;
    if (state.mode === 'real' && i !== state.current + 1) return;
    function advance() {
      state.current = i;
      renderExam();
      window.scrollTo({ top: 0, behavior: 'instant' });
    }
    if (state.mode === 'real' && !isAnswered(QUESTIONS[state.current])) {
      ask('Avançar sem concluir?', 'A questão ou etapas restantes ficarão em branco, sem pontuação. Você não poderá voltar para responder ou revisar.', 'Avançar e bloquear', advance);
    } else advance();
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
      html += '<div class="feedback-box' + (state.mode === 'study' && correctSteps === q.steps.length ? ' is-correct' : '') + '" style="margin-top:var(--space-6)">' +
        '<strong>Cenário concluído</strong>' + (state.mode === 'study' ? 'Você acertou ' + correctSteps + ' de ' + q.steps.length + ' decisões. ' : 'Suas 3 decisões foram registradas. A correção estará no resultado final. ') +
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
        if (chosenIdx !== null && state.mode === 'study') {
          cls += (oi === chosenIdx ? (opt.isBest ? ' correct' : ' incorrect') : '');
          if (oi !== chosenIdx && opt.isBest) cls += ' correct';
        }
        if (chosenIdx !== null && state.mode === 'real' && oi === chosenIdx) cls += ' selected';
        var letter = String.fromCharCode(65 + oi);
        var disabled = chosenIdx !== null ? 'disabled' : '';
        return '<button class="' + cls + '" data-idx="' + oi + '" ' + disabled + '><span class="option__marker">' + letter + '</span><span>' + opt.text + '</span></button>';
      }).join('') + '</div>';

    if (chosenIdx !== null) {
      var chosenOpt = step.options[chosenIdx];
      block += state.mode === 'study' ? '<div class="feedback-box ' + (chosenOpt.isBest ? 'is-correct' : 'is-incorrect') + '">' +
        '<strong>' + (chosenOpt.isBest ? '✓ Melhor decisão' : '✗ Não é a melhor decisão') + '</strong>' + chosenOpt.feedback + '</div>' : '<p class="q-index">Decisão registrada. Correção disponível ao finalizar.</p>';
      // show continue button only if this is the latest answered step (idx === pointer) and there's a next step
      if (idx === state.treePointer[q.id] && idx < q.steps.length - 1) {
        block += '<div style="margin-top:var(--space-4)"><button class="btn btn--sm js-continue" data-next="' + (idx + 1) + '">Continuar cenário →</button></div>';
      }
    }
    block += '</div>';
    return block;
  }

  /* ================= SUBMIT / RESULTS ================= */
  function submitExam() {
    if (state.screen !== 'exam') return;
    if (state.timerHandle) clearInterval(state.timerHandle);
    if (overlay.open) closeDialog();
    state.timeLeftSec = Math.max(0, Math.ceil((state.deadline - Date.now()) / 1000));
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
    var passed = pct + 1e-9 >= DATA.meta.passing_pct;
    var roundedAcertos = Math.round(totalScore * 10) / 10;

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
        '<p class="q-index">' + (state.mode === 'real' ? 'Prova real' : 'Estudo') + ' · Meta do treino: ' + DATA.meta.passing_pct + '% · Tempo utilizado: ' + formatDuration() + '</p>' +
        '<p class="q-index">Pontuação pedagógica: cada múltipla escolha vale 1 ponto; cada árvore vale até 1 ponto, dividido entre suas 3 etapas. Essa pontuação parcial é uma convenção deste simulado, não uma reprodução da metodologia oficial.</p>' +
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
    var usedSec = state.durationMinutes * 60 - state.timeLeftSec;
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
      '<span class="tag">' + THEME_SHORT[q.theme] + '</span></div>' +
      '<p class="q-index review-metadata">' + esc(q.origin || 'Questão autoral') +
      ' · ' + esc(q.bank_id || '') + ' · Dificuldade estimada: ' + esc(q.difficulty || 'Médio') +
      (q.pd_verified ? '<br>Tópico do programa: ' + esc(q.pd) + ' · ' + esc(q.topic) +
        ' · <a href="' + esc(q.references[0]) + '" target="_blank" rel="noopener noreferrer">Consultar programa CPA</a>' : '') +
      '</p>';

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
    ask('Nova tentativa', 'O resultado e as anotações desta tentativa serão apagados. Ao iniciar, um novo conjunto de questões será sorteado.', 'Preparar nova tentativa', function () {
      if (state.timerHandle) clearInterval(state.timerHandle);
      loadExam();
      state.screen = 'start';
      renderStart();
      window.scrollTo({ top: 0, behavior: 'instant' });
    });
  }

  /* ---------------- LOCAL EXAM TOOLS ---------------- */
  function openNotes() {
    showDialog('Bloco de notas', '<label for="exam-notes">Rascunho desta tentativa</label><textarea id="exam-notes" rows="10" maxlength="20000" placeholder="Anote seus cálculos e raciocínios aqui."></textarea><p class="q-index">As notas ficam na memória enquanto esta página estiver aberta. São apagadas ao iniciar uma nova tentativa ou recarregar a página. O cronômetro continua.</p>', function () {
      var notes = document.getElementById('exam-notes');
      notes.value = state.notes;
      notes.addEventListener('input', function () { state.notes = notes.value; });
      notes.focus();
    });
  }

  // Recursive-descent arithmetic parser. Never evaluates JavaScript or HTML.
  function calculate(expression) {
    var normalized = expression.replace(/,/g, '.').replace(/[×x]/g, '*').replace(/÷/g, '/').replace(/\s/g, '');
    if (!normalized || normalized.length > 160) throw Error('Digite uma expressão de até 160 caracteres.');
    var tokens = normalized.match(/(?:\d+(?:\.\d*)?|\.\d+)|[()+*/^%\-]/g);
    if (!tokens || tokens.join('') !== normalized) throw Error('Use apenas números e operações aritméticas.');
    var pos = 0;
    function primary() {
      var value;
      if (tokens[pos] === '(') {
        pos++;
        value = sum();
        if (tokens[pos++] !== ')') throw Error('Confira os parênteses.');
      } else {
        if (!/^(?:\d+(?:\.\d*)?|\.\d+)$/.test(tokens[pos] || '')) throw Error('Confira a expressão.');
        value = Number(tokens[pos++]);
      }
      while (tokens[pos] === '%') { pos++; value /= 100; }
      return value;
    }
    function power() {
      var value = primary();
      if (tokens[pos] === '^') { pos++; value = Math.pow(value, unary()); }
      return value;
    }
    function unary() {
      if (tokens[pos] === '+') { pos++; return unary(); }
      if (tokens[pos] === '-') { pos++; return -unary(); }
      return power();
    }
    function product() {
      var value = unary();
      while (tokens[pos] === '*' || tokens[pos] === '/') {
        var operator = tokens[pos++], right = unary();
        if (operator === '/' && right === 0) throw Error('Não é possível dividir por zero.');
        value = operator === '*' ? value * right : value / right;
      }
      return value;
    }
    function sum() {
      var value = product();
      while (tokens[pos] === '+' || tokens[pos] === '-') {
        var operator = tokens[pos++], right = product();
        value = operator === '+' ? value + right : value - right;
      }
      return value;
    }
    var answer = sum();
    if (pos !== tokens.length || !Number.isFinite(answer)) throw Error('Expressão inválida ou resultado fora do limite.');
    return Number(answer.toPrecision(12));
  }

  function openCalculator() {
    var keys = ['7','8','9','÷','4','5','6','×','1','2','3','-','0',',','%','+','(',')','^','⌫'];
    showDialog('Calculadora', '<form id="calc-form"><label for="calc-input">Expressão</label><input id="calc-input" type="text" inputmode="text" autocomplete="off" maxlength="160" placeholder="Ex.: 1000 × (1 + 10%) ^ 2"><output id="calc-result" aria-live="polite"></output><div class="calc-keys">' +
      keys.map(function (key) { return '<button class="btn btn--secondary" type="button" data-key="' + esc(key) + '">' + key + '</button>'; }).join('') +
      '</div><div class="cta-row"><button class="btn btn--secondary" type="button" id="calc-clear">Limpar</button><button class="btn" type="submit">Calcular</button></div></form><p class="q-index">Aceita parênteses, vírgula decimal, potência (^) e percentual (10% = 0,10). Use Enter para calcular. Ferramenta de treino, não réplica da calculadora oficial; o cronômetro continua.</p>', function () {
      var input = document.getElementById('calc-input');
      var result = document.getElementById('calc-result');
      input.value = state.calcExpression;
      input.addEventListener('input', function () { state.calcExpression = input.value; result.textContent = ''; });
      document.getElementById('calc-form').addEventListener('submit', function (e) {
        e.preventDefault();
        state.calcExpression = input.value;
        try { result.textContent = '= ' + calculate(input.value).toLocaleString('pt-BR', { maximumSignificantDigits: 12 }); }
        catch (error) { result.textContent = error.message; }
      });
      overlay.querySelectorAll('[data-key]').forEach(function (button) {
        button.addEventListener('click', function () {
          var start = input.selectionStart, end = input.selectionEnd;
          var key = button.dataset.key;
          if (key === '⌫') {
            input.setRangeText('', start === end ? Math.max(0, start - 1) : start, end, 'end');
          } else if (input.value.length < 160) {
            input.setRangeText(key, start, end, 'end');
          }
          state.calcExpression = input.value;
          result.textContent = '';
          input.focus();
        });
      });
      document.getElementById('calc-clear').addEventListener('click', function () {
        input.value = ''; state.calcExpression = ''; result.textContent = ''; input.focus();
      });
      input.focus();
    });
  }

  /* ---------------- INIT ---------------- */
  renderStart();
})();
