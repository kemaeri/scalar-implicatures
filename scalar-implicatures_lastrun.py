#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on April 18, 2025, at 10:18
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'scalar-implicatures'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'group': ["native","learner"],
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [2560, 1440]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s_%s' % (expInfo['group'], expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\medej\\Documents\\EXP Semantics Pragmatics\\scalar-implicatures_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    if deviceManager.getDevice('keyWelcome') is None:
        # initialise keyWelcome
        keyWelcome = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyWelcome',
        )
    if deviceManager.getDevice('keySI') is None:
        # initialise keySI
        keySI = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keySI',
        )
    if deviceManager.getDevice('respSI') is None:
        # initialise respSI
        respSI = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='respSI',
        )
    if deviceManager.getDevice('respSI_RT') is None:
        # initialise respSI_RT
        respSI_RT = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='respSI_RT',
        )
    if deviceManager.getDevice('key_instruct') is None:
        # initialise key_instruct
        key_instruct = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_instruct',
        )
    if deviceManager.getDevice('keyLDT') is None:
        # initialise keyLDT
        keyLDT = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyLDT',
        )
    if deviceManager.getDevice('respLDT') is None:
        # initialise respLDT
        respLDT = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='respLDT',
        )
    if deviceManager.getDevice('keyPause') is None:
        # initialise keyPause
        keyPause = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyPause',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "welcome" ---
    textWelcome = visual.TextStim(win=win, name='textWelcome',
        text="***** EXPÉRIENCE EN LIGNE *****\n\nVous avez complété la première tâche. Dans cette expérience, vous accomplirez les deux dernières tâches.\n\n\n[BARRE D'ESPACE]",
        font='Arial',
        units='norm', pos=(0, 0), draggable=False, height=0.08, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    keyWelcome = keyboard.Keyboard(deviceName='keyWelcome')
    
    # --- Initialize components for Routine "taskSI" ---
    instructionsSI = visual.TextStim(win=win, name='instructionsSI',
        text="***** TÂCHE 2: ÉVALUATION DES PHRASES *****\n\nDes phrases vous sont présentées sur l'ecran. Au début, la phrase affichée est incomplète. Appuyez sur la barre d'espace lorsque vous êtes prêt à terminer la phrase. Lisez ensuite le reste de la phrase et répondez à la question. \n\nAppuyez sur [F] pour répondre « non ». \nAppuyez sur [J] pour répondre « oui ».\n\nEffectuez la tâche le plus rapidement et le mieux possible. Tout d'abord, il y a quelques phrases d'entraînement.\n\n[BARRE D'ESPACE]",
        font='Arial',
        units='norm', pos=(0, 0), draggable=False, height=0.08, wrapWidth=1.6, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    keySI = keyboard.Keyboard(deviceName='keySI')
    
    # --- Initialize components for Routine "fix" ---
    fix_rand = visual.TextStim(win=win, name='fix_rand',
        text='+',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "stimSI" ---
    textSI = visual.TextStim(win=win, name='textSI',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=1.6, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    respSI = keyboard.Keyboard(deviceName='respSI')
    
    # --- Initialize components for Routine "stimSI_RT" ---
    textSI_RT = visual.TextStim(win=win, name='textSI_RT',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=1.6, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    respSI_RT = keyboard.Keyboard(deviceName='respSI_RT')
    
    # --- Initialize components for Routine "practiceEnd" ---
    text_norm = visual.TextStim(win=win, name='text_norm',
        text="Voici la fin de l'entraînement. Appuyez sur la barre d'espacement pour commencer la véritable tâche.\n\n[BARRE D'ESPACE]",
        font='Arial',
        units='norm', pos=(0, 0), draggable=False, height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_instruct = keyboard.Keyboard(deviceName='key_instruct')
    
    # --- Initialize components for Routine "fix" ---
    fix_rand = visual.TextStim(win=win, name='fix_rand',
        text='+',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "stimSI" ---
    textSI = visual.TextStim(win=win, name='textSI',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=1.6, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    respSI = keyboard.Keyboard(deviceName='respSI')
    
    # --- Initialize components for Routine "stimSI_RT" ---
    textSI_RT = visual.TextStim(win=win, name='textSI_RT',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=1.6, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    respSI_RT = keyboard.Keyboard(deviceName='respSI_RT')
    
    # --- Initialize components for Routine "taskLDT" ---
    instructionsLDT = visual.TextStim(win=win, name='instructionsLDT',
        text="***** TÂCHE 3: DÉTERMINATION DU NIVEAU DE FRANÇAIS *****\n\nDes mots sont affichés à l'écran. Ils ressemblent tous à des mots français. Certains d'entre eux sont vrais. D'autres sont faux.\n\nAppuyez sur [F] si le mot est faux. \nAppuyez sur [J] si le mot est vrai.\n\n\n[BARRE D'ESPACE]",
        font='Arial',
        units='norm', pos=(0, 0), draggable=False, height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    keyLDT = keyboard.Keyboard(deviceName='keyLDT')
    
    # --- Initialize components for Routine "fix" ---
    fix_rand = visual.TextStim(win=win, name='fix_rand',
        text='+',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "stimLDT" ---
    textLDT = visual.TextStim(win=win, name='textLDT',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    respLDT = keyboard.Keyboard(deviceName='respLDT')
    
    # --- Initialize components for Routine "pause" ---
    # Run 'Begin Experiment' code from codePause
    def multiples(value, length):
        return [*range(value, length*value+1, value)]
    
    breakN = 0
    breakOn = multiples(28,3)
    textPause = visual.TextStim(win=win, name='textPause',
        text=None,
        font='Arial',
        units='norm', pos=(0, 0), draggable=False, height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    keyPause = keyboard.Keyboard(deviceName='keyPause')
    # Run 'Begin Experiment' code from alignPause
    # Code components should usually appear at the top
    # of the routine. This one has to appear after the
    # text component it refers to.
    textPause.alignText= 'center'
    
    # --- Initialize components for Routine "saving" ---
    savingText = visual.TextStim(win=win, name='savingText',
        text="***** FIN *****\n\nJe vous remercie d'avoir complété l'expérience !\n\nLes résultats sont en cours d'enregistrement.\n\n\nVeuillez patienter...",
        font='Arial',
        units='norm', pos=(0, 0), draggable=False, height=0.1, wrapWidth=1.8, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "welcome" ---
    # create an object to store info about Routine welcome
    welcome = data.Routine(
        name='welcome',
        components=[textWelcome, keyWelcome],
    )
    welcome.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for keyWelcome
    keyWelcome.keys = []
    keyWelcome.rt = []
    _keyWelcome_allKeys = []
    # store start times for welcome
    welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    welcome.tStart = globalClock.getTime(format='float')
    welcome.status = STARTED
    thisExp.addData('welcome.started', welcome.tStart)
    welcome.maxDuration = None
    # keep track of which components have finished
    welcomeComponents = welcome.components
    for thisComponent in welcome.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "welcome" ---
    welcome.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textWelcome* updates
        
        # if textWelcome is starting this frame...
        if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textWelcome.frameNStart = frameN  # exact frame index
            textWelcome.tStart = t  # local t and not account for scr refresh
            textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
            # update status
            textWelcome.status = STARTED
            textWelcome.setAutoDraw(True)
        
        # if textWelcome is active this frame...
        if textWelcome.status == STARTED:
            # update params
            pass
        
        # *keyWelcome* updates
        waitOnFlip = False
        
        # if keyWelcome is starting this frame...
        if keyWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyWelcome.frameNStart = frameN  # exact frame index
            keyWelcome.tStart = t  # local t and not account for scr refresh
            keyWelcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyWelcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyWelcome.started')
            # update status
            keyWelcome.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyWelcome.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyWelcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyWelcome.status == STARTED and not waitOnFlip:
            theseKeys = keyWelcome.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _keyWelcome_allKeys.extend(theseKeys)
            if len(_keyWelcome_allKeys):
                keyWelcome.keys = _keyWelcome_allKeys[0].name  # just the first key pressed
                keyWelcome.rt = _keyWelcome_allKeys[0].rt
                keyWelcome.duration = _keyWelcome_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            welcome.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in welcome.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcome" ---
    for thisComponent in welcome.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for welcome
    welcome.tStop = globalClock.getTime(format='float')
    welcome.tStopRefresh = tThisFlipGlobal
    thisExp.addData('welcome.stopped', welcome.tStop)
    # check responses
    if keyWelcome.keys in ['', [], None]:  # No response was made
        keyWelcome.keys = None
    thisExp.addData('keyWelcome.keys',keyWelcome.keys)
    if keyWelcome.keys != None:  # we had a response
        thisExp.addData('keyWelcome.rt', keyWelcome.rt)
        thisExp.addData('keyWelcome.duration', keyWelcome.duration)
    thisExp.nextEntry()
    # the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "taskSI" ---
    # create an object to store info about Routine taskSI
    taskSI = data.Routine(
        name='taskSI',
        components=[instructionsSI, keySI],
    )
    taskSI.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from codeSI_inst
    instructionsSI.alignText = 'left'
    # create starting attributes for keySI
    keySI.keys = []
    keySI.rt = []
    _keySI_allKeys = []
    # store start times for taskSI
    taskSI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    taskSI.tStart = globalClock.getTime(format='float')
    taskSI.status = STARTED
    thisExp.addData('taskSI.started', taskSI.tStart)
    taskSI.maxDuration = None
    # keep track of which components have finished
    taskSIComponents = taskSI.components
    for thisComponent in taskSI.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "taskSI" ---
    taskSI.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsSI* updates
        
        # if instructionsSI is starting this frame...
        if instructionsSI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructionsSI.frameNStart = frameN  # exact frame index
            instructionsSI.tStart = t  # local t and not account for scr refresh
            instructionsSI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionsSI, 'tStartRefresh')  # time at next scr refresh
            # update status
            instructionsSI.status = STARTED
            instructionsSI.setAutoDraw(True)
        
        # if instructionsSI is active this frame...
        if instructionsSI.status == STARTED:
            # update params
            pass
        
        # *keySI* updates
        waitOnFlip = False
        
        # if keySI is starting this frame...
        if keySI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keySI.frameNStart = frameN  # exact frame index
            keySI.tStart = t  # local t and not account for scr refresh
            keySI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keySI, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keySI.started')
            # update status
            keySI.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keySI.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keySI.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keySI.status == STARTED and not waitOnFlip:
            theseKeys = keySI.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _keySI_allKeys.extend(theseKeys)
            if len(_keySI_allKeys):
                keySI.keys = _keySI_allKeys[0].name  # just the first key pressed
                keySI.rt = _keySI_allKeys[0].rt
                keySI.duration = _keySI_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            taskSI.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in taskSI.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "taskSI" ---
    for thisComponent in taskSI.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for taskSI
    taskSI.tStop = globalClock.getTime(format='float')
    taskSI.tStopRefresh = tThisFlipGlobal
    thisExp.addData('taskSI.stopped', taskSI.tStop)
    # check responses
    if keySI.keys in ['', [], None]:  # No response was made
        keySI.keys = None
    thisExp.addData('keySI.keys',keySI.keys)
    if keySI.keys != None:  # we had a response
        thisExp.addData('keySI.rt', keySI.rt)
        thisExp.addData('keySI.duration', keySI.duration)
    thisExp.nextEntry()
    # the Routine "taskSI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practice = data.TrialHandler2(
        name='practice',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('resources/practiceMainTask.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(practice)  # add the loop to the experiment
    thisPractice = practice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            globals()[paramName] = thisPractice[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPractice in practice:
        currentLoop = practice
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
        if thisPractice != None:
            for paramName in thisPractice:
                globals()[paramName] = thisPractice[paramName]
        
        # --- Prepare to start Routine "fix" ---
        # create an object to store info about Routine fix
        fix = data.Routine(
            name='fix',
            components=[fix_rand],
        )
        fix.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for fix
        fix.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        fix.tStart = globalClock.getTime(format='float')
        fix.status = STARTED
        thisExp.addData('fix.started', fix.tStart)
        fix.maxDuration = None
        # keep track of which components have finished
        fixComponents = fix.components
        for thisComponent in fix.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fix" ---
        # if trial has changed, end Routine now
        if isinstance(practice, data.TrialHandler2) and thisPractice.thisN != practice.thisTrial.thisN:
            continueRoutine = False
        fix.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix_rand* updates
            
            # if fix_rand is starting this frame...
            if fix_rand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_rand.frameNStart = frameN  # exact frame index
                fix_rand.tStart = t  # local t and not account for scr refresh
                fix_rand.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_rand, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_rand.started')
                # update status
                fix_rand.status = STARTED
                fix_rand.setAutoDraw(True)
            
            # if fix_rand is active this frame...
            if fix_rand.status == STARTED:
                # update params
                pass
            
            # if fix_rand is stopping this frame...
            if fix_rand.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_rand.tStartRefresh + random()+0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_rand.tStop = t  # not accounting for scr refresh
                    fix_rand.tStopRefresh = tThisFlipGlobal  # on global time
                    fix_rand.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix_rand.stopped')
                    # update status
                    fix_rand.status = FINISHED
                    fix_rand.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                fix.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fix.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fix" ---
        for thisComponent in fix.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for fix
        fix.tStop = globalClock.getTime(format='float')
        fix.tStopRefresh = tThisFlipGlobal
        thisExp.addData('fix.stopped', fix.tStop)
        # the Routine "fix" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "stimSI" ---
        # create an object to store info about Routine stimSI
        stimSI = data.Routine(
            name='stimSI',
            components=[textSI, respSI],
        )
        stimSI.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from codeSI
        textSI.setText("")
        
        phrase1 = '%s dit : « %s %s %s. »'%(speaker, subject, verb, scale_first)
        phrase2 = 'Pouvez-vous en conclure ce qui suit ?'
        phrase3 = '...'
        phrase4 = "[BARRE D'ESPACE]"
        
        # Run 'Begin Routine' code from alignSI
        textSI.alignText = "center"
        # create starting attributes for respSI
        respSI.keys = []
        respSI.rt = []
        _respSI_allKeys = []
        # store start times for stimSI
        stimSI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        stimSI.tStart = globalClock.getTime(format='float')
        stimSI.status = STARTED
        thisExp.addData('stimSI.started', stimSI.tStart)
        stimSI.maxDuration = None
        # keep track of which components have finished
        stimSIComponents = stimSI.components
        for thisComponent in stimSI.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "stimSI" ---
        # if trial has changed, end Routine now
        if isinstance(practice, data.TrialHandler2) and thisPractice.thisN != practice.thisTrial.thisN:
            continueRoutine = False
        stimSI.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textSI* updates
            
            # if textSI is starting this frame...
            if textSI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textSI.frameNStart = frameN  # exact frame index
                textSI.tStart = t  # local t and not account for scr refresh
                textSI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textSI, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textSI.started')
                # update status
                textSI.status = STARTED
                textSI.setAutoDraw(True)
            
            # if textSI is active this frame...
            if textSI.status == STARTED:
                # update params
                textSI.setText('%s\n\n\n%s\n\n\n%s\n\n\n%s'%(phrase1, phrase2, phrase3, phrase4), log=False)
            
            # *respSI* updates
            waitOnFlip = False
            
            # if respSI is starting this frame...
            if respSI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                respSI.frameNStart = frameN  # exact frame index
                respSI.tStart = t  # local t and not account for scr refresh
                respSI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(respSI, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'respSI.started')
                # update status
                respSI.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(respSI.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(respSI.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if respSI.status == STARTED and not waitOnFlip:
                theseKeys = respSI.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _respSI_allKeys.extend(theseKeys)
                if len(_respSI_allKeys):
                    respSI.keys = _respSI_allKeys[-1].name  # just the last key pressed
                    respSI.rt = _respSI_allKeys[-1].rt
                    respSI.duration = _respSI_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                stimSI.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stimSI.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "stimSI" ---
        for thisComponent in stimSI.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for stimSI
        stimSI.tStop = globalClock.getTime(format='float')
        stimSI.tStopRefresh = tThisFlipGlobal
        thisExp.addData('stimSI.stopped', stimSI.tStop)
        # check responses
        if respSI.keys in ['', [], None]:  # No response was made
            respSI.keys = None
        practice.addData('respSI.keys',respSI.keys)
        if respSI.keys != None:  # we had a response
            practice.addData('respSI.rt', respSI.rt)
            practice.addData('respSI.duration', respSI.duration)
        # the Routine "stimSI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "stimSI_RT" ---
        # create an object to store info about Routine stimSI_RT
        stimSI_RT = data.Routine(
            name='stimSI_RT',
            components=[textSI_RT, respSI_RT],
        )
        stimSI_RT.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from codeSI_RT
        textSI_RT.setText("")
        
        phrase1 = '%s dit : « %s %s %s. »'%(speaker, subject, verb, scale_first)
        phrase2 = 'Pouvez-vous en conclure ce qui suit ?'
        phrase3 = 'Selon %s, %s n\'est pas %s.'%(speaker, subject, scale_second)
        phrase4 = '[F] non \t\t [J] oui'
        
        textSI_RT.setText('%s\n\n\n%s\n\n\n%s\n\n\n%s'%(phrase1, phrase2, phrase3, phrase4))
        # Run 'Begin Routine' code from alignSI_RT
        textSI_RT.alignText = "center"
        # create starting attributes for respSI_RT
        respSI_RT.keys = []
        respSI_RT.rt = []
        _respSI_RT_allKeys = []
        # store start times for stimSI_RT
        stimSI_RT.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        stimSI_RT.tStart = globalClock.getTime(format='float')
        stimSI_RT.status = STARTED
        thisExp.addData('stimSI_RT.started', stimSI_RT.tStart)
        stimSI_RT.maxDuration = None
        # keep track of which components have finished
        stimSI_RTComponents = stimSI_RT.components
        for thisComponent in stimSI_RT.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "stimSI_RT" ---
        # if trial has changed, end Routine now
        if isinstance(practice, data.TrialHandler2) and thisPractice.thisN != practice.thisTrial.thisN:
            continueRoutine = False
        stimSI_RT.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textSI_RT* updates
            
            # if textSI_RT is starting this frame...
            if textSI_RT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textSI_RT.frameNStart = frameN  # exact frame index
                textSI_RT.tStart = t  # local t and not account for scr refresh
                textSI_RT.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textSI_RT, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textSI_RT.started')
                # update status
                textSI_RT.status = STARTED
                textSI_RT.setAutoDraw(True)
            
            # if textSI_RT is active this frame...
            if textSI_RT.status == STARTED:
                # update params
                pass
            
            # *respSI_RT* updates
            waitOnFlip = False
            
            # if respSI_RT is starting this frame...
            if respSI_RT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                respSI_RT.frameNStart = frameN  # exact frame index
                respSI_RT.tStart = t  # local t and not account for scr refresh
                respSI_RT.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(respSI_RT, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'respSI_RT.started')
                # update status
                respSI_RT.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(respSI_RT.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(respSI_RT.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if respSI_RT.status == STARTED and not waitOnFlip:
                theseKeys = respSI_RT.getKeys(keyList=['f', 'j'], ignoreKeys=["escape"], waitRelease=False)
                _respSI_RT_allKeys.extend(theseKeys)
                if len(_respSI_RT_allKeys):
                    respSI_RT.keys = _respSI_RT_allKeys[-1].name  # just the last key pressed
                    respSI_RT.rt = _respSI_RT_allKeys[-1].rt
                    respSI_RT.duration = _respSI_RT_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                stimSI_RT.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stimSI_RT.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "stimSI_RT" ---
        for thisComponent in stimSI_RT.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for stimSI_RT
        stimSI_RT.tStop = globalClock.getTime(format='float')
        stimSI_RT.tStopRefresh = tThisFlipGlobal
        thisExp.addData('stimSI_RT.stopped', stimSI_RT.tStop)
        # check responses
        if respSI_RT.keys in ['', [], None]:  # No response was made
            respSI_RT.keys = None
        practice.addData('respSI_RT.keys',respSI_RT.keys)
        if respSI_RT.keys != None:  # we had a response
            practice.addData('respSI_RT.rt', respSI_RT.rt)
            practice.addData('respSI_RT.duration', respSI_RT.duration)
        # the Routine "stimSI_RT" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'practice'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "practiceEnd" ---
    # create an object to store info about Routine practiceEnd
    practiceEnd = data.Routine(
        name='practiceEnd',
        components=[text_norm, key_instruct],
    )
    practiceEnd.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_instruct
    key_instruct.keys = []
    key_instruct.rt = []
    _key_instruct_allKeys = []
    # store start times for practiceEnd
    practiceEnd.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    practiceEnd.tStart = globalClock.getTime(format='float')
    practiceEnd.status = STARTED
    thisExp.addData('practiceEnd.started', practiceEnd.tStart)
    practiceEnd.maxDuration = None
    # keep track of which components have finished
    practiceEndComponents = practiceEnd.components
    for thisComponent in practiceEnd.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "practiceEnd" ---
    practiceEnd.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_norm* updates
        
        # if text_norm is starting this frame...
        if text_norm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_norm.frameNStart = frameN  # exact frame index
            text_norm.tStart = t  # local t and not account for scr refresh
            text_norm.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_norm, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_norm.status = STARTED
            text_norm.setAutoDraw(True)
        
        # if text_norm is active this frame...
        if text_norm.status == STARTED:
            # update params
            pass
        
        # *key_instruct* updates
        waitOnFlip = False
        
        # if key_instruct is starting this frame...
        if key_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_instruct.frameNStart = frameN  # exact frame index
            key_instruct.tStart = t  # local t and not account for scr refresh
            key_instruct.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_instruct, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_instruct.started')
            # update status
            key_instruct.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_instruct.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_instruct.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_instruct.status == STARTED and not waitOnFlip:
            theseKeys = key_instruct.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_instruct_allKeys.extend(theseKeys)
            if len(_key_instruct_allKeys):
                key_instruct.keys = _key_instruct_allKeys[0].name  # just the first key pressed
                key_instruct.rt = _key_instruct_allKeys[0].rt
                key_instruct.duration = _key_instruct_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            practiceEnd.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceEnd.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practiceEnd" ---
    for thisComponent in practiceEnd.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for practiceEnd
    practiceEnd.tStop = globalClock.getTime(format='float')
    practiceEnd.tStopRefresh = tThisFlipGlobal
    thisExp.addData('practiceEnd.stopped', practiceEnd.tStop)
    # check responses
    if key_instruct.keys in ['', [], None]:  # No response was made
        key_instruct.keys = None
    thisExp.addData('key_instruct.keys',key_instruct.keys)
    if key_instruct.keys != None:  # we had a response
        thisExp.addData('key_instruct.rt', key_instruct.rt)
        thisExp.addData('key_instruct.duration', key_instruct.duration)
    thisExp.nextEntry()
    # the Routine "practiceEnd" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    implicatures = data.TrialHandler2(
        name='implicatures',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('resources/stimuliMainTask.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(implicatures)  # add the loop to the experiment
    thisImplicature = implicatures.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisImplicature.rgb)
    if thisImplicature != None:
        for paramName in thisImplicature:
            globals()[paramName] = thisImplicature[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisImplicature in implicatures:
        currentLoop = implicatures
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisImplicature.rgb)
        if thisImplicature != None:
            for paramName in thisImplicature:
                globals()[paramName] = thisImplicature[paramName]
        
        # --- Prepare to start Routine "fix" ---
        # create an object to store info about Routine fix
        fix = data.Routine(
            name='fix',
            components=[fix_rand],
        )
        fix.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for fix
        fix.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        fix.tStart = globalClock.getTime(format='float')
        fix.status = STARTED
        thisExp.addData('fix.started', fix.tStart)
        fix.maxDuration = None
        # keep track of which components have finished
        fixComponents = fix.components
        for thisComponent in fix.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fix" ---
        # if trial has changed, end Routine now
        if isinstance(implicatures, data.TrialHandler2) and thisImplicature.thisN != implicatures.thisTrial.thisN:
            continueRoutine = False
        fix.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix_rand* updates
            
            # if fix_rand is starting this frame...
            if fix_rand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_rand.frameNStart = frameN  # exact frame index
                fix_rand.tStart = t  # local t and not account for scr refresh
                fix_rand.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_rand, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_rand.started')
                # update status
                fix_rand.status = STARTED
                fix_rand.setAutoDraw(True)
            
            # if fix_rand is active this frame...
            if fix_rand.status == STARTED:
                # update params
                pass
            
            # if fix_rand is stopping this frame...
            if fix_rand.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_rand.tStartRefresh + random()+0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_rand.tStop = t  # not accounting for scr refresh
                    fix_rand.tStopRefresh = tThisFlipGlobal  # on global time
                    fix_rand.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix_rand.stopped')
                    # update status
                    fix_rand.status = FINISHED
                    fix_rand.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                fix.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fix.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fix" ---
        for thisComponent in fix.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for fix
        fix.tStop = globalClock.getTime(format='float')
        fix.tStopRefresh = tThisFlipGlobal
        thisExp.addData('fix.stopped', fix.tStop)
        # the Routine "fix" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "stimSI" ---
        # create an object to store info about Routine stimSI
        stimSI = data.Routine(
            name='stimSI',
            components=[textSI, respSI],
        )
        stimSI.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from codeSI
        textSI.setText("")
        
        phrase1 = '%s dit : « %s %s %s. »'%(speaker, subject, verb, scale_first)
        phrase2 = 'Pouvez-vous en conclure ce qui suit ?'
        phrase3 = '...'
        phrase4 = "[BARRE D'ESPACE]"
        
        # Run 'Begin Routine' code from alignSI
        textSI.alignText = "center"
        # create starting attributes for respSI
        respSI.keys = []
        respSI.rt = []
        _respSI_allKeys = []
        # store start times for stimSI
        stimSI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        stimSI.tStart = globalClock.getTime(format='float')
        stimSI.status = STARTED
        thisExp.addData('stimSI.started', stimSI.tStart)
        stimSI.maxDuration = None
        # keep track of which components have finished
        stimSIComponents = stimSI.components
        for thisComponent in stimSI.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "stimSI" ---
        # if trial has changed, end Routine now
        if isinstance(implicatures, data.TrialHandler2) and thisImplicature.thisN != implicatures.thisTrial.thisN:
            continueRoutine = False
        stimSI.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textSI* updates
            
            # if textSI is starting this frame...
            if textSI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textSI.frameNStart = frameN  # exact frame index
                textSI.tStart = t  # local t and not account for scr refresh
                textSI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textSI, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textSI.started')
                # update status
                textSI.status = STARTED
                textSI.setAutoDraw(True)
            
            # if textSI is active this frame...
            if textSI.status == STARTED:
                # update params
                textSI.setText('%s\n\n\n%s\n\n\n%s\n\n\n%s'%(phrase1, phrase2, phrase3, phrase4), log=False)
            
            # *respSI* updates
            waitOnFlip = False
            
            # if respSI is starting this frame...
            if respSI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                respSI.frameNStart = frameN  # exact frame index
                respSI.tStart = t  # local t and not account for scr refresh
                respSI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(respSI, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'respSI.started')
                # update status
                respSI.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(respSI.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(respSI.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if respSI.status == STARTED and not waitOnFlip:
                theseKeys = respSI.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _respSI_allKeys.extend(theseKeys)
                if len(_respSI_allKeys):
                    respSI.keys = _respSI_allKeys[-1].name  # just the last key pressed
                    respSI.rt = _respSI_allKeys[-1].rt
                    respSI.duration = _respSI_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                stimSI.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stimSI.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "stimSI" ---
        for thisComponent in stimSI.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for stimSI
        stimSI.tStop = globalClock.getTime(format='float')
        stimSI.tStopRefresh = tThisFlipGlobal
        thisExp.addData('stimSI.stopped', stimSI.tStop)
        # check responses
        if respSI.keys in ['', [], None]:  # No response was made
            respSI.keys = None
        implicatures.addData('respSI.keys',respSI.keys)
        if respSI.keys != None:  # we had a response
            implicatures.addData('respSI.rt', respSI.rt)
            implicatures.addData('respSI.duration', respSI.duration)
        # the Routine "stimSI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "stimSI_RT" ---
        # create an object to store info about Routine stimSI_RT
        stimSI_RT = data.Routine(
            name='stimSI_RT',
            components=[textSI_RT, respSI_RT],
        )
        stimSI_RT.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from codeSI_RT
        textSI_RT.setText("")
        
        phrase1 = '%s dit : « %s %s %s. »'%(speaker, subject, verb, scale_first)
        phrase2 = 'Pouvez-vous en conclure ce qui suit ?'
        phrase3 = 'Selon %s, %s n\'est pas %s.'%(speaker, subject, scale_second)
        phrase4 = '[F] non \t\t [J] oui'
        
        textSI_RT.setText('%s\n\n\n%s\n\n\n%s\n\n\n%s'%(phrase1, phrase2, phrase3, phrase4))
        # Run 'Begin Routine' code from alignSI_RT
        textSI_RT.alignText = "center"
        # create starting attributes for respSI_RT
        respSI_RT.keys = []
        respSI_RT.rt = []
        _respSI_RT_allKeys = []
        # store start times for stimSI_RT
        stimSI_RT.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        stimSI_RT.tStart = globalClock.getTime(format='float')
        stimSI_RT.status = STARTED
        thisExp.addData('stimSI_RT.started', stimSI_RT.tStart)
        stimSI_RT.maxDuration = None
        # keep track of which components have finished
        stimSI_RTComponents = stimSI_RT.components
        for thisComponent in stimSI_RT.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "stimSI_RT" ---
        # if trial has changed, end Routine now
        if isinstance(implicatures, data.TrialHandler2) and thisImplicature.thisN != implicatures.thisTrial.thisN:
            continueRoutine = False
        stimSI_RT.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textSI_RT* updates
            
            # if textSI_RT is starting this frame...
            if textSI_RT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textSI_RT.frameNStart = frameN  # exact frame index
                textSI_RT.tStart = t  # local t and not account for scr refresh
                textSI_RT.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textSI_RT, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textSI_RT.started')
                # update status
                textSI_RT.status = STARTED
                textSI_RT.setAutoDraw(True)
            
            # if textSI_RT is active this frame...
            if textSI_RT.status == STARTED:
                # update params
                pass
            
            # *respSI_RT* updates
            waitOnFlip = False
            
            # if respSI_RT is starting this frame...
            if respSI_RT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                respSI_RT.frameNStart = frameN  # exact frame index
                respSI_RT.tStart = t  # local t and not account for scr refresh
                respSI_RT.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(respSI_RT, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'respSI_RT.started')
                # update status
                respSI_RT.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(respSI_RT.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(respSI_RT.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if respSI_RT.status == STARTED and not waitOnFlip:
                theseKeys = respSI_RT.getKeys(keyList=['f', 'j'], ignoreKeys=["escape"], waitRelease=False)
                _respSI_RT_allKeys.extend(theseKeys)
                if len(_respSI_RT_allKeys):
                    respSI_RT.keys = _respSI_RT_allKeys[-1].name  # just the last key pressed
                    respSI_RT.rt = _respSI_RT_allKeys[-1].rt
                    respSI_RT.duration = _respSI_RT_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                stimSI_RT.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stimSI_RT.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "stimSI_RT" ---
        for thisComponent in stimSI_RT.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for stimSI_RT
        stimSI_RT.tStop = globalClock.getTime(format='float')
        stimSI_RT.tStopRefresh = tThisFlipGlobal
        thisExp.addData('stimSI_RT.stopped', stimSI_RT.tStop)
        # check responses
        if respSI_RT.keys in ['', [], None]:  # No response was made
            respSI_RT.keys = None
        implicatures.addData('respSI_RT.keys',respSI_RT.keys)
        if respSI_RT.keys != None:  # we had a response
            implicatures.addData('respSI_RT.rt', respSI_RT.rt)
            implicatures.addData('respSI_RT.duration', respSI_RT.duration)
        # the Routine "stimSI_RT" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'implicatures'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "taskLDT" ---
    # create an object to store info about Routine taskLDT
    taskLDT = data.Routine(
        name='taskLDT',
        components=[instructionsLDT, keyLDT],
    )
    taskLDT.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for keyLDT
    keyLDT.keys = []
    keyLDT.rt = []
    _keyLDT_allKeys = []
    # Run 'Begin Routine' code from codeLDT_ins
    instructionsLDT.alignText = 'left'
    # store start times for taskLDT
    taskLDT.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    taskLDT.tStart = globalClock.getTime(format='float')
    taskLDT.status = STARTED
    thisExp.addData('taskLDT.started', taskLDT.tStart)
    taskLDT.maxDuration = None
    # keep track of which components have finished
    taskLDTComponents = taskLDT.components
    for thisComponent in taskLDT.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "taskLDT" ---
    taskLDT.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsLDT* updates
        
        # if instructionsLDT is starting this frame...
        if instructionsLDT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructionsLDT.frameNStart = frameN  # exact frame index
            instructionsLDT.tStart = t  # local t and not account for scr refresh
            instructionsLDT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionsLDT, 'tStartRefresh')  # time at next scr refresh
            # update status
            instructionsLDT.status = STARTED
            instructionsLDT.setAutoDraw(True)
        
        # if instructionsLDT is active this frame...
        if instructionsLDT.status == STARTED:
            # update params
            pass
        
        # *keyLDT* updates
        waitOnFlip = False
        
        # if keyLDT is starting this frame...
        if keyLDT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyLDT.frameNStart = frameN  # exact frame index
            keyLDT.tStart = t  # local t and not account for scr refresh
            keyLDT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyLDT, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyLDT.started')
            # update status
            keyLDT.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyLDT.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyLDT.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyLDT.status == STARTED and not waitOnFlip:
            theseKeys = keyLDT.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _keyLDT_allKeys.extend(theseKeys)
            if len(_keyLDT_allKeys):
                keyLDT.keys = _keyLDT_allKeys[0].name  # just the first key pressed
                keyLDT.rt = _keyLDT_allKeys[0].rt
                keyLDT.duration = _keyLDT_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            taskLDT.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in taskLDT.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "taskLDT" ---
    for thisComponent in taskLDT.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for taskLDT
    taskLDT.tStop = globalClock.getTime(format='float')
    taskLDT.tStopRefresh = tThisFlipGlobal
    thisExp.addData('taskLDT.stopped', taskLDT.tStop)
    # check responses
    if keyLDT.keys in ['', [], None]:  # No response was made
        keyLDT.keys = None
    thisExp.addData('keyLDT.keys',keyLDT.keys)
    if keyLDT.keys != None:  # we had a response
        thisExp.addData('keyLDT.rt', keyLDT.rt)
        thisExp.addData('keyLDT.duration', keyLDT.duration)
    thisExp.nextEntry()
    # the Routine "taskLDT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    lexTALE = data.TrialHandler2(
        name='lexTALE',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('resources/stimuliLexTALE.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(lexTALE)  # add the loop to the experiment
    thisLexTALE = lexTALE.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLexTALE.rgb)
    if thisLexTALE != None:
        for paramName in thisLexTALE:
            globals()[paramName] = thisLexTALE[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLexTALE in lexTALE:
        currentLoop = lexTALE
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLexTALE.rgb)
        if thisLexTALE != None:
            for paramName in thisLexTALE:
                globals()[paramName] = thisLexTALE[paramName]
        
        # --- Prepare to start Routine "fix" ---
        # create an object to store info about Routine fix
        fix = data.Routine(
            name='fix',
            components=[fix_rand],
        )
        fix.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for fix
        fix.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        fix.tStart = globalClock.getTime(format='float')
        fix.status = STARTED
        thisExp.addData('fix.started', fix.tStart)
        fix.maxDuration = None
        # keep track of which components have finished
        fixComponents = fix.components
        for thisComponent in fix.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fix" ---
        # if trial has changed, end Routine now
        if isinstance(lexTALE, data.TrialHandler2) and thisLexTALE.thisN != lexTALE.thisTrial.thisN:
            continueRoutine = False
        fix.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix_rand* updates
            
            # if fix_rand is starting this frame...
            if fix_rand.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_rand.frameNStart = frameN  # exact frame index
                fix_rand.tStart = t  # local t and not account for scr refresh
                fix_rand.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_rand, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_rand.started')
                # update status
                fix_rand.status = STARTED
                fix_rand.setAutoDraw(True)
            
            # if fix_rand is active this frame...
            if fix_rand.status == STARTED:
                # update params
                pass
            
            # if fix_rand is stopping this frame...
            if fix_rand.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_rand.tStartRefresh + random()+0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_rand.tStop = t  # not accounting for scr refresh
                    fix_rand.tStopRefresh = tThisFlipGlobal  # on global time
                    fix_rand.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix_rand.stopped')
                    # update status
                    fix_rand.status = FINISHED
                    fix_rand.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                fix.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fix.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fix" ---
        for thisComponent in fix.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for fix
        fix.tStop = globalClock.getTime(format='float')
        fix.tStopRefresh = tThisFlipGlobal
        thisExp.addData('fix.stopped', fix.tStop)
        # the Routine "fix" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "stimLDT" ---
        # create an object to store info about Routine stimLDT
        stimLDT = data.Routine(
            name='stimLDT',
            components=[textLDT, respLDT],
        )
        stimLDT.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        textLDT.setText(word)
        # create starting attributes for respLDT
        respLDT.keys = []
        respLDT.rt = []
        _respLDT_allKeys = []
        # store start times for stimLDT
        stimLDT.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        stimLDT.tStart = globalClock.getTime(format='float')
        stimLDT.status = STARTED
        thisExp.addData('stimLDT.started', stimLDT.tStart)
        stimLDT.maxDuration = None
        # keep track of which components have finished
        stimLDTComponents = stimLDT.components
        for thisComponent in stimLDT.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "stimLDT" ---
        # if trial has changed, end Routine now
        if isinstance(lexTALE, data.TrialHandler2) and thisLexTALE.thisN != lexTALE.thisTrial.thisN:
            continueRoutine = False
        stimLDT.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textLDT* updates
            
            # if textLDT is starting this frame...
            if textLDT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textLDT.frameNStart = frameN  # exact frame index
                textLDT.tStart = t  # local t and not account for scr refresh
                textLDT.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textLDT, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textLDT.started')
                # update status
                textLDT.status = STARTED
                textLDT.setAutoDraw(True)
            
            # if textLDT is active this frame...
            if textLDT.status == STARTED:
                # update params
                pass
            
            # *respLDT* updates
            waitOnFlip = False
            
            # if respLDT is starting this frame...
            if respLDT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                respLDT.frameNStart = frameN  # exact frame index
                respLDT.tStart = t  # local t and not account for scr refresh
                respLDT.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(respLDT, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'respLDT.started')
                # update status
                respLDT.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(respLDT.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(respLDT.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if respLDT.status == STARTED and not waitOnFlip:
                theseKeys = respLDT.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
                _respLDT_allKeys.extend(theseKeys)
                if len(_respLDT_allKeys):
                    respLDT.keys = _respLDT_allKeys[-1].name  # just the last key pressed
                    respLDT.rt = _respLDT_allKeys[-1].rt
                    respLDT.duration = _respLDT_allKeys[-1].duration
                    # was this correct?
                    if (respLDT.keys == str(corrAns)) or (respLDT.keys == corrAns):
                        respLDT.corr = 1
                    else:
                        respLDT.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                stimLDT.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stimLDT.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "stimLDT" ---
        for thisComponent in stimLDT.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for stimLDT
        stimLDT.tStop = globalClock.getTime(format='float')
        stimLDT.tStopRefresh = tThisFlipGlobal
        thisExp.addData('stimLDT.stopped', stimLDT.tStop)
        # check responses
        if respLDT.keys in ['', [], None]:  # No response was made
            respLDT.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               respLDT.corr = 1;  # correct non-response
            else:
               respLDT.corr = 0;  # failed to respond (incorrectly)
        # store data for lexTALE (TrialHandler)
        lexTALE.addData('respLDT.keys',respLDT.keys)
        lexTALE.addData('respLDT.corr', respLDT.corr)
        if respLDT.keys != None:  # we had a response
            lexTALE.addData('respLDT.rt', respLDT.rt)
            lexTALE.addData('respLDT.duration', respLDT.duration)
        # the Routine "stimLDT" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "pause" ---
        # create an object to store info about Routine pause
        pause = data.Routine(
            name='pause',
            components=[textPause, keyPause],
        )
        pause.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from codePause
        if lexTALE.thisN+1 in breakOn[:-1]:
            continueRoutine = True
            breakN += 1
            text = 'Ceci était le bloc %s des %s. Faites une pause et appuyez sur la barre d\'espacement pour continuer.'%(breakN,len(breakOn))
            textPause.setText(text)
        else:
            continueRoutine = False
        # create starting attributes for keyPause
        keyPause.keys = []
        keyPause.rt = []
        _keyPause_allKeys = []
        # store start times for pause
        pause.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        pause.tStart = globalClock.getTime(format='float')
        pause.status = STARTED
        thisExp.addData('pause.started', pause.tStart)
        pause.maxDuration = None
        # keep track of which components have finished
        pauseComponents = pause.components
        for thisComponent in pause.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "pause" ---
        # if trial has changed, end Routine now
        if isinstance(lexTALE, data.TrialHandler2) and thisLexTALE.thisN != lexTALE.thisTrial.thisN:
            continueRoutine = False
        pause.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textPause* updates
            
            # if textPause is starting this frame...
            if textPause.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textPause.frameNStart = frameN  # exact frame index
                textPause.tStart = t  # local t and not account for scr refresh
                textPause.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textPause, 'tStartRefresh')  # time at next scr refresh
                # update status
                textPause.status = STARTED
                textPause.setAutoDraw(True)
            
            # if textPause is active this frame...
            if textPause.status == STARTED:
                # update params
                pass
            
            # *keyPause* updates
            waitOnFlip = False
            
            # if keyPause is starting this frame...
            if keyPause.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                keyPause.frameNStart = frameN  # exact frame index
                keyPause.tStart = t  # local t and not account for scr refresh
                keyPause.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyPause, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'keyPause.started')
                # update status
                keyPause.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(keyPause.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(keyPause.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if keyPause.status == STARTED and not waitOnFlip:
                theseKeys = keyPause.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _keyPause_allKeys.extend(theseKeys)
                if len(_keyPause_allKeys):
                    keyPause.keys = _keyPause_allKeys[0].name  # just the first key pressed
                    keyPause.rt = _keyPause_allKeys[0].rt
                    keyPause.duration = _keyPause_allKeys[0].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                pause.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pause.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pause" ---
        for thisComponent in pause.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for pause
        pause.tStop = globalClock.getTime(format='float')
        pause.tStopRefresh = tThisFlipGlobal
        thisExp.addData('pause.stopped', pause.tStop)
        # check responses
        if keyPause.keys in ['', [], None]:  # No response was made
            keyPause.keys = None
        lexTALE.addData('keyPause.keys',keyPause.keys)
        if keyPause.keys != None:  # we had a response
            lexTALE.addData('keyPause.rt', keyPause.rt)
            lexTALE.addData('keyPause.duration', keyPause.duration)
        # the Routine "pause" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'lexTALE'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "saving" ---
    # create an object to store info about Routine saving
    saving = data.Routine(
        name='saving',
        components=[savingText],
    )
    saving.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for saving
    saving.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    saving.tStart = globalClock.getTime(format='float')
    saving.status = STARTED
    thisExp.addData('saving.started', saving.tStart)
    saving.maxDuration = None
    # keep track of which components have finished
    savingComponents = saving.components
    for thisComponent in saving.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "saving" ---
    saving.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *savingText* updates
        
        # if savingText is starting this frame...
        if savingText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            savingText.frameNStart = frameN  # exact frame index
            savingText.tStart = t  # local t and not account for scr refresh
            savingText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(savingText, 'tStartRefresh')  # time at next scr refresh
            # update status
            savingText.status = STARTED
            savingText.setAutoDraw(True)
        
        # if savingText is active this frame...
        if savingText.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            saving.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in saving.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "saving" ---
    for thisComponent in saving.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for saving
    saving.tStop = globalClock.getTime(format='float')
    saving.tStopRefresh = tThisFlipGlobal
    thisExp.addData('saving.stopped', saving.tStop)
    thisExp.nextEntry()
    # the Routine "saving" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
