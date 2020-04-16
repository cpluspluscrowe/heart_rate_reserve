

recovery = ("recovery",0,70)
general_aerobic = ("general aerobic",62, 75)
endurance = ("endurance",65, 78)
lactate_threshold = ("lactate threshold",75,88)
vo2_max = ("vo2max",92,97)
training_types = [recovery,general_aerobic, endurance, lactate_threshold, vo2_max]

def calculate_target_heart_rate(percent, hrr, resting_hr):
    return hrr * percent/100 + resting_hr

def get_zones(resting_hr):
    max_hr = 197
    hrr = max_hr - resting_hr
    for training_type in training_types:
        name, low, high = training_type
        low_hr = calculate_target_heart_rate(low, hrr, resting_hr)
        high_hr =calculate_target_heart_rate(high, hrr, resting_hr)
        print("{0}: {1} - {2}".format(name, low_hr, high_hr))


for x in range(48,58):
    get_zones(x)
    print()
