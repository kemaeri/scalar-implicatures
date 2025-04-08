/**************************** 
 * Scalar-Implicatures *
 ****************************/


// store info about the experiment session:
let expName = 'scalar-implicatures';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'group': ["native", "learner"],
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(welcomeRoutineBegin());
flowScheduler.add(welcomeRoutineEachFrame());
flowScheduler.add(welcomeRoutineEnd());
flowScheduler.add(taskSIRoutineBegin());
flowScheduler.add(taskSIRoutineEachFrame());
flowScheduler.add(taskSIRoutineEnd());
const implicaturesLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(implicaturesLoopBegin(implicaturesLoopScheduler));
flowScheduler.add(implicaturesLoopScheduler);
flowScheduler.add(implicaturesLoopEnd);



flowScheduler.add(taskLDTRoutineBegin());
flowScheduler.add(taskLDTRoutineEachFrame());
flowScheduler.add(taskLDTRoutineEnd());
const lexTALELoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(lexTALELoopBegin(lexTALELoopScheduler));
flowScheduler.add(lexTALELoopScheduler);
flowScheduler.add(lexTALELoopEnd);



flowScheduler.add(savingRoutineBegin());
flowScheduler.add(savingRoutineEachFrame());
flowScheduler.add(savingRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Merci de votre patience et de votre participation.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Merci de votre patience et de votre participation.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'resources/stimuliMainTask.xlsx', 'path': 'resources/stimuliMainTask.xlsx'},
    {'name': 'resources/stimuliLexTALE.xlsx', 'path': 'resources/stimuliLexTALE.xlsx'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var welcomeClock;
var textWelcome;
var keyWelcome;
var taskSIClock;
var instructionsSI;
var keySI;
var fixClock;
var fix_rand;
var stimSIClock;
var textSI;
var respSI;
var taskLDTClock;
var instructionsLDT;
var keyLDT;
var stimLDTClock;
var textLDT;
var respLDT;
var savingClock;
var savingText;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "welcome"
  welcomeClock = new util.Clock();
  textWelcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'textWelcome',
    text: "***** EXPÉRIENCE EN LIGNE *****\n\nVous avez complété la première tâche. Dans cette expérience, vous accomplirez les deux dernières tâches.\n\n\nAppuyez sur la barre d'espacement pour passer à la tâche suivante.",
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], draggable: false, height: 0.1,  wrapWidth: 1.8, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  keyWelcome = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "taskSI"
  taskSIClock = new util.Clock();
  instructionsSI = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructionsSI',
    text: "***** TÂCHE 2: ÉVALUATION DES PHRASES *****\n\nUne phrase vous sera présentée et vous répondrez à une question sur cette phrase à l'aide du clavier.\n\nAppuyez sur la touche F pour répondre « non ». \nAppuyez sur la touche J pour répondre « oui ».\n\n\nAppuyez sur la barre d'espacement pour démarrer.",
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], draggable: false, height: 0.1,  wrapWidth: 1.8, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  keySI = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fix"
  fixClock = new util.Clock();
  fix_rand = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix_rand',
    text: '+',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "stimSI"
  stimSIClock = new util.Clock();
  textSI = new visual.TextStim({
    win: psychoJS.window,
    name: 'textSI',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: 1.2, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  respSI = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "taskLDT"
  taskLDTClock = new util.Clock();
  instructionsLDT = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructionsLDT',
    text: "***** TÂCHE 3: DÉTERMINATION DU NIVEAU DE FRANÇAIS *****\n\nDes mots seront affichés à l'écran. Ils ressembleront tous à des mots français. Certains d'entre eux sont vrais. D'autres sont faux.\n\nAppuyez sur la touche F  si le mot est faux. \nAppuyez sur la touche J si le mot est vrai.\n\n\nAppuyez sur la barre d'espacement pour démarrer.",
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], draggable: false, height: 0.1,  wrapWidth: 1.8, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  keyLDT = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "stimLDT"
  stimLDTClock = new util.Clock();
  textLDT = new visual.TextStim({
    win: psychoJS.window,
    name: 'textLDT',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  respLDT = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "saving"
  savingClock = new util.Clock();
  savingText = new visual.TextStim({
    win: psychoJS.window,
    name: 'savingText',
    text: "***** FIN *****\n\nJe vous remercie d'avoir complété l'expérience !\n\nLes résultats sont en cours d'enregistrement.\n\nVeuillez patienter...",
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], draggable: false, height: 0.1,  wrapWidth: 1.8, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var welcomeMaxDurationReached;
var _keyWelcome_allKeys;
var welcomeMaxDuration;
var welcomeComponents;
function welcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'welcome' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    welcomeClock.reset();
    routineTimer.reset();
    welcomeMaxDurationReached = false;
    // update component parameters for each repeat
    keyWelcome.keys = undefined;
    keyWelcome.rt = undefined;
    _keyWelcome_allKeys = [];
    psychoJS.experiment.addData('welcome.started', globalClock.getTime());
    welcomeMaxDuration = null
    // keep track of which components have finished
    welcomeComponents = [];
    welcomeComponents.push(textWelcome);
    welcomeComponents.push(keyWelcome);
    
    welcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function welcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'welcome' ---
    // get current time
    t = welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textWelcome* updates
    if (t >= 0.0 && textWelcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textWelcome.tStart = t;  // (not accounting for frame time here)
      textWelcome.frameNStart = frameN;  // exact frame index
      
      textWelcome.setAutoDraw(true);
    }
    
    
    // *keyWelcome* updates
    if (t >= 0.0 && keyWelcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyWelcome.tStart = t;  // (not accounting for frame time here)
      keyWelcome.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyWelcome.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyWelcome.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyWelcome.clearEvents(); });
    }
    
    if (keyWelcome.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyWelcome.getKeys({keyList: ['space'], waitRelease: false});
      _keyWelcome_allKeys = _keyWelcome_allKeys.concat(theseKeys);
      if (_keyWelcome_allKeys.length > 0) {
        keyWelcome.keys = _keyWelcome_allKeys[0].name;  // just the first key pressed
        keyWelcome.rt = _keyWelcome_allKeys[0].rt;
        keyWelcome.duration = _keyWelcome_allKeys[0].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    welcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'welcome' ---
    welcomeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('welcome.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(keyWelcome.corr, level);
    }
    psychoJS.experiment.addData('keyWelcome.keys', keyWelcome.keys);
    if (typeof keyWelcome.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyWelcome.rt', keyWelcome.rt);
        psychoJS.experiment.addData('keyWelcome.duration', keyWelcome.duration);
        routineTimer.reset();
        }
    
    keyWelcome.stop();
    // the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var taskSIMaxDurationReached;
var _keySI_allKeys;
var taskSIMaxDuration;
var taskSIComponents;
function taskSIRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'taskSI' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    taskSIClock.reset();
    routineTimer.reset();
    taskSIMaxDurationReached = false;
    // update component parameters for each repeat
    keySI.keys = undefined;
    keySI.rt = undefined;
    _keySI_allKeys = [];
    psychoJS.experiment.addData('taskSI.started', globalClock.getTime());
    taskSIMaxDuration = null
    // keep track of which components have finished
    taskSIComponents = [];
    taskSIComponents.push(instructionsSI);
    taskSIComponents.push(keySI);
    
    taskSIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function taskSIRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'taskSI' ---
    // get current time
    t = taskSIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructionsSI* updates
    if (t >= 0.0 && instructionsSI.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructionsSI.tStart = t;  // (not accounting for frame time here)
      instructionsSI.frameNStart = frameN;  // exact frame index
      
      instructionsSI.setAutoDraw(true);
    }
    
    
    // *keySI* updates
    if (t >= 0.0 && keySI.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keySI.tStart = t;  // (not accounting for frame time here)
      keySI.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keySI.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keySI.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keySI.clearEvents(); });
    }
    
    if (keySI.status === PsychoJS.Status.STARTED) {
      let theseKeys = keySI.getKeys({keyList: ['space'], waitRelease: false});
      _keySI_allKeys = _keySI_allKeys.concat(theseKeys);
      if (_keySI_allKeys.length > 0) {
        keySI.keys = _keySI_allKeys[0].name;  // just the first key pressed
        keySI.rt = _keySI_allKeys[0].rt;
        keySI.duration = _keySI_allKeys[0].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    taskSIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function taskSIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'taskSI' ---
    taskSIComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('taskSI.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(keySI.corr, level);
    }
    psychoJS.experiment.addData('keySI.keys', keySI.keys);
    if (typeof keySI.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keySI.rt', keySI.rt);
        psychoJS.experiment.addData('keySI.duration', keySI.duration);
        routineTimer.reset();
        }
    
    keySI.stop();
    // the Routine "taskSI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var implicatures;
function implicaturesLoopBegin(implicaturesLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    implicatures = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'resources/stimuliMainTask.xlsx',
      seed: undefined, name: 'implicatures'
    });
    psychoJS.experiment.addLoop(implicatures); // add the loop to the experiment
    currentLoop = implicatures;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    implicatures.forEach(function() {
      snapshot = implicatures.getSnapshot();
    
      implicaturesLoopScheduler.add(importConditions(snapshot));
      implicaturesLoopScheduler.add(fixRoutineBegin(snapshot));
      implicaturesLoopScheduler.add(fixRoutineEachFrame());
      implicaturesLoopScheduler.add(fixRoutineEnd(snapshot));
      implicaturesLoopScheduler.add(stimSIRoutineBegin(snapshot));
      implicaturesLoopScheduler.add(stimSIRoutineEachFrame());
      implicaturesLoopScheduler.add(stimSIRoutineEnd(snapshot));
      implicaturesLoopScheduler.add(implicaturesLoopEndIteration(implicaturesLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function implicaturesLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(implicatures);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function implicaturesLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var lexTALE;
function lexTALELoopBegin(lexTALELoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    lexTALE = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'resources/stimuliLexTALE.xlsx',
      seed: undefined, name: 'lexTALE'
    });
    psychoJS.experiment.addLoop(lexTALE); // add the loop to the experiment
    currentLoop = lexTALE;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    lexTALE.forEach(function() {
      snapshot = lexTALE.getSnapshot();
    
      lexTALELoopScheduler.add(importConditions(snapshot));
      lexTALELoopScheduler.add(fixRoutineBegin(snapshot));
      lexTALELoopScheduler.add(fixRoutineEachFrame());
      lexTALELoopScheduler.add(fixRoutineEnd(snapshot));
      lexTALELoopScheduler.add(stimLDTRoutineBegin(snapshot));
      lexTALELoopScheduler.add(stimLDTRoutineEachFrame());
      lexTALELoopScheduler.add(stimLDTRoutineEnd(snapshot));
      lexTALELoopScheduler.add(lexTALELoopEndIteration(lexTALELoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function lexTALELoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(lexTALE);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function lexTALELoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var fixMaxDurationReached;
var fixMaxDuration;
var fixComponents;
function fixRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fix' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    fixClock.reset();
    routineTimer.reset();
    fixMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('fix.started', globalClock.getTime());
    fixMaxDuration = null
    // keep track of which components have finished
    fixComponents = [];
    fixComponents.push(fix_rand);
    
    fixComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function fixRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fix' ---
    // get current time
    t = fixClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix_rand* updates
    if (t >= 0.0 && fix_rand.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix_rand.tStart = t;  // (not accounting for frame time here)
      fix_rand.frameNStart = frameN;  // exact frame index
      
      fix_rand.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + (Math.random() + 0.3) - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (fix_rand.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix_rand.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fixComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fix' ---
    fixComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('fix.stopped', globalClock.getTime());
    // the Routine "fix" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var stimSIMaxDurationReached;
var text;
var _respSI_allKeys;
var stimSIMaxDuration;
var stimSIComponents;
function stimSIRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'stimSI' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    stimSIClock.reset();
    routineTimer.reset();
    stimSIMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from codeSI
    textSI.setText("");
    text = `${speaker} dit :  « ${sentence}. »
    
    Est-ce que vous pouvez en conclure que, selon ${speaker}, ${negation} ?
    
    [f] non     [j] oui`;
    
    respSI.keys = undefined;
    respSI.rt = undefined;
    _respSI_allKeys = [];
    psychoJS.experiment.addData('stimSI.started', globalClock.getTime());
    stimSIMaxDuration = null
    // keep track of which components have finished
    stimSIComponents = [];
    stimSIComponents.push(textSI);
    stimSIComponents.push(respSI);
    
    stimSIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function stimSIRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'stimSI' ---
    // get current time
    t = stimSIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (textSI.status === PsychoJS.Status.STARTED){ // only update if being drawn
      textSI.setText(text, false);
    }
    
    // *textSI* updates
    if (t >= 0.0 && textSI.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textSI.tStart = t;  // (not accounting for frame time here)
      textSI.frameNStart = frameN;  // exact frame index
      
      textSI.setAutoDraw(true);
    }
    
    
    // *respSI* updates
    if (t >= 0.0 && respSI.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      respSI.tStart = t;  // (not accounting for frame time here)
      respSI.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { respSI.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { respSI.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { respSI.clearEvents(); });
    }
    
    if (respSI.status === PsychoJS.Status.STARTED) {
      let theseKeys = respSI.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _respSI_allKeys = _respSI_allKeys.concat(theseKeys);
      if (_respSI_allKeys.length > 0) {
        respSI.keys = _respSI_allKeys[_respSI_allKeys.length - 1].name;  // just the last key pressed
        respSI.rt = _respSI_allKeys[_respSI_allKeys.length - 1].rt;
        respSI.duration = _respSI_allKeys[_respSI_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    stimSIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stimSIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'stimSI' ---
    stimSIComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('stimSI.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(respSI.corr, level);
    }
    psychoJS.experiment.addData('respSI.keys', respSI.keys);
    if (typeof respSI.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('respSI.rt', respSI.rt);
        psychoJS.experiment.addData('respSI.duration', respSI.duration);
        routineTimer.reset();
        }
    
    respSI.stop();
    // the Routine "stimSI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var taskLDTMaxDurationReached;
var _keyLDT_allKeys;
var taskLDTMaxDuration;
var taskLDTComponents;
function taskLDTRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'taskLDT' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    taskLDTClock.reset();
    routineTimer.reset();
    taskLDTMaxDurationReached = false;
    // update component parameters for each repeat
    keyLDT.keys = undefined;
    keyLDT.rt = undefined;
    _keyLDT_allKeys = [];
    psychoJS.experiment.addData('taskLDT.started', globalClock.getTime());
    taskLDTMaxDuration = null
    // keep track of which components have finished
    taskLDTComponents = [];
    taskLDTComponents.push(instructionsLDT);
    taskLDTComponents.push(keyLDT);
    
    taskLDTComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function taskLDTRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'taskLDT' ---
    // get current time
    t = taskLDTClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructionsLDT* updates
    if (t >= 0.0 && instructionsLDT.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructionsLDT.tStart = t;  // (not accounting for frame time here)
      instructionsLDT.frameNStart = frameN;  // exact frame index
      
      instructionsLDT.setAutoDraw(true);
    }
    
    
    // *keyLDT* updates
    if (t >= 0.0 && keyLDT.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyLDT.tStart = t;  // (not accounting for frame time here)
      keyLDT.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyLDT.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyLDT.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyLDT.clearEvents(); });
    }
    
    if (keyLDT.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyLDT.getKeys({keyList: ['space'], waitRelease: false});
      _keyLDT_allKeys = _keyLDT_allKeys.concat(theseKeys);
      if (_keyLDT_allKeys.length > 0) {
        keyLDT.keys = _keyLDT_allKeys[0].name;  // just the first key pressed
        keyLDT.rt = _keyLDT_allKeys[0].rt;
        keyLDT.duration = _keyLDT_allKeys[0].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    taskLDTComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function taskLDTRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'taskLDT' ---
    taskLDTComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('taskLDT.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(keyLDT.corr, level);
    }
    psychoJS.experiment.addData('keyLDT.keys', keyLDT.keys);
    if (typeof keyLDT.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyLDT.rt', keyLDT.rt);
        psychoJS.experiment.addData('keyLDT.duration', keyLDT.duration);
        routineTimer.reset();
        }
    
    keyLDT.stop();
    // the Routine "taskLDT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var stimLDTMaxDurationReached;
var _respLDT_allKeys;
var stimLDTMaxDuration;
var stimLDTComponents;
function stimLDTRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'stimLDT' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    stimLDTClock.reset();
    routineTimer.reset();
    stimLDTMaxDurationReached = false;
    // update component parameters for each repeat
    textLDT.setText(word);
    respLDT.keys = undefined;
    respLDT.rt = undefined;
    _respLDT_allKeys = [];
    psychoJS.experiment.addData('stimLDT.started', globalClock.getTime());
    stimLDTMaxDuration = null
    // keep track of which components have finished
    stimLDTComponents = [];
    stimLDTComponents.push(textLDT);
    stimLDTComponents.push(respLDT);
    
    stimLDTComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function stimLDTRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'stimLDT' ---
    // get current time
    t = stimLDTClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textLDT* updates
    if (t >= 0.0 && textLDT.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textLDT.tStart = t;  // (not accounting for frame time here)
      textLDT.frameNStart = frameN;  // exact frame index
      
      textLDT.setAutoDraw(true);
    }
    
    
    // *respLDT* updates
    if (t >= 0.0 && respLDT.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      respLDT.tStart = t;  // (not accounting for frame time here)
      respLDT.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { respLDT.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { respLDT.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { respLDT.clearEvents(); });
    }
    
    if (respLDT.status === PsychoJS.Status.STARTED) {
      let theseKeys = respLDT.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _respLDT_allKeys = _respLDT_allKeys.concat(theseKeys);
      if (_respLDT_allKeys.length > 0) {
        respLDT.keys = _respLDT_allKeys[_respLDT_allKeys.length - 1].name;  // just the last key pressed
        respLDT.rt = _respLDT_allKeys[_respLDT_allKeys.length - 1].rt;
        respLDT.duration = _respLDT_allKeys[_respLDT_allKeys.length - 1].duration;
        // was this correct?
        if (respLDT.keys == corrAns) {
            respLDT.corr = 1;
        } else {
            respLDT.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    stimLDTComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stimLDTRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'stimLDT' ---
    stimLDTComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('stimLDT.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (respLDT.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         respLDT.corr = 1;  // correct non-response
      } else {
         respLDT.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(respLDT.corr, level);
    }
    psychoJS.experiment.addData('respLDT.keys', respLDT.keys);
    psychoJS.experiment.addData('respLDT.corr', respLDT.corr);
    if (typeof respLDT.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('respLDT.rt', respLDT.rt);
        psychoJS.experiment.addData('respLDT.duration', respLDT.duration);
        routineTimer.reset();
        }
    
    respLDT.stop();
    // the Routine "stimLDT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var savingMaxDurationReached;
var savingMaxDuration;
var savingComponents;
function savingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'saving' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    savingClock.reset();
    routineTimer.reset();
    savingMaxDurationReached = false;
    // update component parameters for each repeat
    // Disable downloading results to browser
    psychoJS._saveResults = 0;
    
    // Generate filename for results
    let filename = "group_" + expInfo["group"] + "_participant_" + expInfo["participant"] + "_" + psychoJS._experiment._experimentName + '_' + psychoJS._experiment._datetime;
    
    // Convert data object to JSON
    let dataJSON = JSON.stringify(psychoJS.experiment._trialsData);
    
    // Send data to OSF
    fetch("https://pipe.jspsych.org/api/data/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Accept: "*/*",
          },
          body: JSON.stringify({
            experimentID: "pGFiZFN0CmV4",
            filename: `${filename}.json`,
            data: dataJSON,
          }),
    }).then(response => response.json()).then(data => {
        console.log(data);
        quitPsychoJS();
    });
    
    psychoJS.experiment.addData('saving.started', globalClock.getTime());
    savingMaxDuration = null
    // keep track of which components have finished
    savingComponents = [];
    savingComponents.push(savingText);
    
    savingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function savingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'saving' ---
    // get current time
    t = savingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *savingText* updates
    if (t >= 0.0 && savingText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      savingText.tStart = t;  // (not accounting for frame time here)
      savingText.frameNStart = frameN;  // exact frame index
      
      savingText.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    savingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function savingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'saving' ---
    savingComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('saving.stopped', globalClock.getTime());
    // the Routine "saving" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
