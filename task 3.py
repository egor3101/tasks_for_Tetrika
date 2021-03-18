example = {
    'lesson': [1594663200, 1594666800],
    'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
    'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
}


def appearance(intervals):
    start_time_pupil = intervals["pupil"][0]
    end_time_pupil = intervals["pupil"][-1]
    start_time_tutor = intervals["tutor"][0]
    end_time_tutor = intervals["tutor"][-1]

    pupil_set = {i for i in range(start_time_pupil, end_time_pupil + 1)}
    tutor_set = {i for i in range(start_time_tutor, end_time_tutor + 1)}
    answer = len(tutor_set & pupil_set)
    return answer


print(appearance(example))

# Мнтересное задание. Из всех представленных заданий мне понравилось больше всего это.
