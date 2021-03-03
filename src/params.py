file_path = 'data/hedepy_test/treatmentTherapistShort.wav'
window_size = 0.025  # 25ms
window_overlap = 0.015  # 15ms
remove_pitches_size = 0.35  # seconds
hesitations_max_size_max_size = 2  # seconds
pre_emphasis_coefficient = 0.97
energy_threshold = 70
number_of_lpc_coefficients = 10
displayEnergy = False
save_to = 'output'
with_gmm = False

# get pitches sizes in segments
remove_pitches_size = int(remove_pitches_size / window_size)
hesitations_max_size_max_size = int(hesitations_max_size_max_size / window_size)
