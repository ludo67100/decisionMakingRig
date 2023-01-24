# =============================================================================
# TASK PARAMETER DEFINITION (should appear on GUI) init trial objects values
# =============================================================================
# SOUND, AMBIENT SENSOR, AND VIDEO RECORDINGS
RECORD_SOUND = True
RECORD_AMBIENT_SENSOR_DATA = True
# REWARDS
AUTOMATIC_CALIBRATION = True  # Wether to look for a calibration session and func to define the valve opening time  # noqa
CALIBRATION_VALUE = (
    0.067  # 0.067calibration value for 3ul of target reward amount (ignored if automatic ON)  # noqa
)
REWARD_AMOUNT = 3.0  # (µl) Amount of reward to be delivered upon correct choice each trial (overwitten if adaptive ON)  # noqa
REWARD_TYPE = "Water 15% Sucrose"  # Water, Water 10% Sucrose, Water 15% Sucrose, Water 2% Citric Acid (Guo et al.. PLoS One 2014)  # noqa
# TASK
NTRIALS = 2000  # Number of trials for the current session
USE_AUTOMATIC_STOPPING_CRITERIONS = (
    True  # Weather to check for the Automatic stopping criterions or not  # noqa
)
USE_VISUAL_STIMULUS = True  # Run the visual stim in bonsai
BONSAI_EDITOR = False  # Whether to open the visual stim Bonsai editor or not
REPEAT_ON_ERROR = False
# STATE TIMERS
QUIESCENCE_THRESHOLDS = [-2,2]  # degree
QUIESCENT_PERIOD = 0.2  # + x, where x~exp(0.35), t ∈ 0.2 <= R <= 0.5
INTERACTIVE_DELAY = 0.0  # (s) how long after stim onset the CL starts
RESPONSE_WINDOW = 60  # Time to move the wheel after go tone (seconds)
ITI_CORRECT = 1  # how long the stim should stay visible after CORRECT choice
ITI_ERROR = 2  # how long the stim should stay visible after ERROR choice
# VISUAL STIM
STIM_FREQ = 0.10  # Probably constant - NOT IN USE
STIM_ANGLE = 0.0  # Vertical orientation of Gabor patch - NOT IN USE
STIM_SIGMA = 7.0  # (azimuth_degree) Size of Gabor patch
STIM_GAIN = 4.0  # (azimuth_degree/mm) Gain of the RE to stimulus movement
SYNC_SQUARE_X = 1.33
SYNC_SQUARE_Y = -1.03
# BLOCKS
BLOCK_INIT_5050 = True
BLOCK_PROBABILITY_SET = [1,0]
BLOCK_LEN_FACTOR = 60
BLOCK_LEN_MIN = 20
BLOCK_LEN_MAX = 100
# POSITIONS
STIM_POSITIONS = [-35,35]  # Rewarded postion (JV)(deg)
# CONTRASTS
CONTRAST_SET = [1.0]  # Full contrast set
CONTRAST_SET_PROBABILITY_TYPE = (
    "uniform"  # 'biased' or 'uniform'. Will half the probability of drawing a 0.  # noqa
)
# SOUNDS
SOFT_SOUND = "xonar"  # Use software sound 'xonar', 'sysdefault' or None for BpodSoundCard  # noqa
SOUND_BOARD_BPOD_PORT = "Serial3"  # (on Bpod) - Ignored if using SOFT_SOUND
WHITE_NOISE_DURATION = 0.5  # Length of noise burst
WHITE_NOISE_AMPLITUDE = 0.0725 # original 0.05
GO_TONE_DURATION = 0.1  # Length of tone
GO_TONE_FREQUENCY = 5000  # 5KHz
GO_TONE_AMPLITUDE = 0.0  # [0->1] 0.0272 for 70dB SPL Xonar
# POOP COUNT LOGGING
POOP_COUNT = True  # Wether to ask for a poop count at the end of the session

#================================================================================================
#==========================Dynamic choice parameters LS May 2022================================
#================================================================================================

#===REWARD TO THE LEFT ONLY================================================================
#PRESET_REWARD_DIRECTIONS = [-1 for x in range(NTRIALS)]


#===REWARD TO THE RIGHT ONLY===============================================================
PRESET_REWARD_DIRECTIONS = [1 for x in range(NTRIALS)]

#===CUSTOM LIST================================================================================
#TODO : For some reason trial 1 is skipped by system, hence the 0 value in arg[1]
#PRESET_REWARD_DIRECTIONS = [-1,0,1,1,1,1,1,1,-1,1,-1,-1,-1]

#Day 1reversal Bloc=10, threshold=70, ctoff=20
#Amount of trials in block + expected performance

TRIALS_IN_DYNAMIC_BLOC = 10

#How many trials should be correct in the block (in%)

EXPECTED_SUCCESS_RATE = 70

#CUTOFF : mouse will get a reward after n failed trials anyway TODO - should be >>> TRIALS_IN_DYNAMIC_BLOC
DYNAMIC_CUTOFF = 20

#Generate probabilities 
PROB_REWARD_SIDE = 0.8
PROB_NON_REWARD_SITE = 0.2