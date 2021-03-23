# input file path
file_path = 'data_to_delete/transcribed/same_room/session2/stereo.wav'
transcription_path = 'data_to_delete/transcribed/same_room/session2/transcription.trs'
# preprocessing
pre_emphasis_coefficient = 0.97

window_size = 0.02  # 20ms
window_overlap = 0.01  # 10ms
window_stride = window_size - window_overlap  # 10ms

# mfcc
frequency_resolution = 512
cepstral_coef_count = 12
lifter = 22
delta_neighbours = 2

# energy vad
energy_threshold_interval = 0.1  # 100ms
med_filter = 0.1  # 250 ms
min_silence_likelihood = 0.95  # 95%

# vad hmm
vad_min_speech_dur = 1
vad_loop_probability = 0.95

# diarization
gmm_max_iterations = 100
gmm_error_rate = 1e-3

propagation_size = 10
prop_coef = 0.5
mean_filter_diar = 100  # Each segment represents 10 ms -> 100 segments = 1s
median_filter_diar = 100

likelihood_percentile = 20  # Take 20% of highest likelihood frames
model_means_shift = 0.05

# output folder
output_folder = 'output'

# tests
transcription_plot = True
collar_size = 250  # ms

# OLD
hesitations_max_size_max_size = 2  # seconds
number_of_lpc_coefficients = 10
displayEnergy = False

# get pitches sizes in segments
# remove_pitches_size = int(remove_pitches_size / window_size)
hesitations_max_size_max_size = int(hesitations_max_size_max_size / window_size)
