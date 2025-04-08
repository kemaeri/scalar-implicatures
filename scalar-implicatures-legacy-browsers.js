/**************************** 
 * Scalar-Implicatures *
 ****************************/


// store info about the experiment session:
let expName = 'scalar-implicatures';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
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
flowScheduler.add(insSIRoutineBegin());
flowScheduler.add(insSIRoutineEachFrame());
flowScheduler.add(insSIRoutineEnd());
const implicaturesLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(implicaturesLoopBegin(implicaturesLoopScheduler));
flowScheduler.add(implicaturesLoopScheduler);
flowScheduler.add(implicaturesLoopEnd);



flowScheduler.add(insLexRoutineBegin());
flowScheduler.add(insLexRoutineEachFrame());
flowScheduler.add(insLexRoutineEnd());
const lexiTALELoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(lexiTALELoopBegin(lexiTALELoopScheduler));
flowScheduler.add(lexiTALELoopScheduler);
flowScheduler.add(lexiTALELoopEnd);



flowScheduler.add(savingRoutineBegin());
flowScheduler.add(savingRoutineEachFrame());
flowScheduler.add(savingRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

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
var insSIClock;
var instructionsSI;
var keySI;
var fixClock;
var fix_rand;
var trialClock;
var stimSI;
var respSI;
var insLexClock;
var text_norm_3;
var key_instruct_3;
var decisionClock;
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
    text: 'Any text\n\nincluding line breaks\n\nThis text component is white, so change the colour if you have a white background. It does not save the onset and offset time, but has been left justified with a wrap width of 1.8 norm units.\n\nPress the spacebar to continue',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], draggable: false, height: 0.1,  wrapWidth: 1.8, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  keyWelcome = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "insSI"
  insSIClock = new util.Clock();
  instructionsSI = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructionsSI',
    text: 'Any text\n\nincluding line breaks\n\nThis text component is white, so change the colour if you have a white background. It does not save the onset and offset time, but has been left justified with a wrap width of 1.8 norm units.\n\nPress the spacebar to continue',
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
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  stimSI = new visual.TextStim({
    win: psychoJS.window,
    name: 'stimSI',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: 1.2, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  respSI = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "insLex"
  insLexClock = new util.Clock();
  text_norm_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_norm_3',
    text: 'Any text\n\nincluding line breaks\n\nThis text component is white, so change the colour if you have a white background. It does not save the onset and offset time, but has been left justified with a wrap width of 1.8 norm units.\n\nPress the spacebar to continue',
    font: 'Arial',
    units: 'norm', 
    pos: [0, 0], draggable: false, height: 0.1,  wrapWidth: 1.8, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_instruct_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "decision"
  decisionClock = new util.Clock();
  // Initialize components for Routine "saving"
  savingClock = new util.Clock();
  savingText = new visual.TextStim({
    win: psychoJS.window,
    name: 'savingText',
    text: "Merci d'avoir complété l'expérience !\n\nLes résultats sont en cours d'enregistrement.\n\nVeuillez patienter.",
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


var insSIMaxDurationReached;
var _keySI_allKeys;
var insSIMaxDuration;
var insSIComponents;
function insSIRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'insSI' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    insSIClock.reset();
    routineTimer.reset();
    insSIMaxDurationReached = false;
    // update component parameters for each repeat
    keySI.keys = undefined;
    keySI.rt = undefined;
    _keySI_allKeys = [];
    psychoJS.experiment.addData('insSI.started', globalClock.getTime());
    insSIMaxDuration = null
    // keep track of which components have finished
    insSIComponents = [];
    insSIComponents.push(instructionsSI);
    insSIComponents.push(keySI);
    
    insSIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function insSIRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'insSI' ---
    // get current time
    t = insSIClock.getTime();
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
    insSIComponents.forEach( function(thisComponent) {
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


function insSIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'insSI' ---
    insSIComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('insSI.stopped', globalClock.getTime());
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
    // the Routine "insSI" was not non-slip safe, so reset the non-slip timer
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
      implicaturesLoopScheduler.add(trialRoutineBegin(snapshot));
      implicaturesLoopScheduler.add(trialRoutineEachFrame());
      implicaturesLoopScheduler.add(trialRoutineEnd(snapshot));
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


var lexiTALE;
function lexiTALELoopBegin(lexiTALELoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    lexiTALE = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'resources/stimuliLexTALE.xlsx',
      seed: undefined, name: 'lexiTALE'
    });
    psychoJS.experiment.addLoop(lexiTALE); // add the loop to the experiment
    currentLoop = lexiTALE;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    lexiTALE.forEach(function() {
      snapshot = lexiTALE.getSnapshot();
    
      lexiTALELoopScheduler.add(importConditions(snapshot));
      lexiTALELoopScheduler.add(fixRoutineBegin(snapshot));
      lexiTALELoopScheduler.add(fixRoutineEachFrame());
      lexiTALELoopScheduler.add(fixRoutineEnd(snapshot));
      lexiTALELoopScheduler.add(decisionRoutineBegin(snapshot));
      lexiTALELoopScheduler.add(decisionRoutineEachFrame());
      lexiTALELoopScheduler.add(decisionRoutineEnd(snapshot));
      lexiTALELoopScheduler.add(lexiTALELoopEndIteration(lexiTALELoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function lexiTALELoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(lexiTALE);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function lexiTALELoopEndIteration(scheduler, snapshot) {
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
    
    frameRemains = 0.0 + (Math.random() + 1) - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
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


var trialMaxDurationReached;
var _respSI_allKeys;
var text;
var trialMaxDuration;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    trialClock.reset();
    routineTimer.reset();
    trialMaxDurationReached = false;
    // update component parameters for each repeat
    stimSI.setText('');
    respSI.keys = undefined;
    respSI.rt = undefined;
    _respSI_allKeys = [];
    // Run 'Begin Routine' code from codeSI
    text = `${speaker} dit :  « ${sentence}. »
    Est-ce que vous pouvez en conclure que, 
    selon ${speaker}, ${negation} ?
    
    [f] non\t\t[j] oui`;
    
    stimSI.setText(text);
    psychoJS.experiment.addData('trial.started', globalClock.getTime());
    trialMaxDuration = null
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(stimSI);
    trialComponents.push(respSI);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *stimSI* updates
    if (t >= 0.0 && stimSI.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stimSI.tStart = t;  // (not accounting for frame time here)
      stimSI.frameNStart = frameN;  // exact frame index
      
      stimSI.setAutoDraw(true);
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
    trialComponents.forEach( function(thisComponent) {
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


function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('trial.stopped', globalClock.getTime());
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
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var insLexMaxDurationReached;
var _key_instruct_3_allKeys;
var insLexMaxDuration;
var insLexComponents;
function insLexRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'insLex' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    insLexClock.reset();
    routineTimer.reset();
    insLexMaxDurationReached = false;
    // update component parameters for each repeat
    key_instruct_3.keys = undefined;
    key_instruct_3.rt = undefined;
    _key_instruct_3_allKeys = [];
    psychoJS.experiment.addData('insLex.started', globalClock.getTime());
    insLexMaxDuration = null
    // keep track of which components have finished
    insLexComponents = [];
    insLexComponents.push(text_norm_3);
    insLexComponents.push(key_instruct_3);
    
    insLexComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function insLexRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'insLex' ---
    // get current time
    t = insLexClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_norm_3* updates
    if (t >= 0.0 && text_norm_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_norm_3.tStart = t;  // (not accounting for frame time here)
      text_norm_3.frameNStart = frameN;  // exact frame index
      
      text_norm_3.setAutoDraw(true);
    }
    
    
    // *key_instruct_3* updates
    if (t >= 0.0 && key_instruct_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_instruct_3.tStart = t;  // (not accounting for frame time here)
      key_instruct_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_instruct_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_instruct_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_instruct_3.clearEvents(); });
    }
    
    if (key_instruct_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_instruct_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_instruct_3_allKeys = _key_instruct_3_allKeys.concat(theseKeys);
      if (_key_instruct_3_allKeys.length > 0) {
        key_instruct_3.keys = _key_instruct_3_allKeys[0].name;  // just the first key pressed
        key_instruct_3.rt = _key_instruct_3_allKeys[0].rt;
        key_instruct_3.duration = _key_instruct_3_allKeys[0].duration;
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
    insLexComponents.forEach( function(thisComponent) {
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


function insLexRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'insLex' ---
    insLexComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('insLex.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_instruct_3.corr, level);
    }
    psychoJS.experiment.addData('key_instruct_3.keys', key_instruct_3.keys);
    if (typeof key_instruct_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_instruct_3.rt', key_instruct_3.rt);
        psychoJS.experiment.addData('key_instruct_3.duration', key_instruct_3.duration);
        routineTimer.reset();
        }
    
    key_instruct_3.stop();
    // the Routine "insLex" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var decisionMaxDurationReached;
var decisionMaxDuration;
var decisionComponents;
function decisionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'decision' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    decisionClock.reset();
    routineTimer.reset();
    decisionMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('decision.started', globalClock.getTime());
    decisionMaxDuration = null
    // keep track of which components have finished
    decisionComponents = [];
    
    decisionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function decisionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'decision' ---
    // get current time
    t = decisionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    decisionComponents.forEach( function(thisComponent) {
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


function decisionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'decision' ---
    decisionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('decision.stopped', globalClock.getTime());
    // the Routine "decision" was not non-slip safe, so reset the non-slip timer
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
    let filename = "list_" + expInfo["list_no"] + "_participant_" + expInfo["participant"] + "_" + psychoJS._experiment._experimentName + '_' + psychoJS._experiment._datetime;
    
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
