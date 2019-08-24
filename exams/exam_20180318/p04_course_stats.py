semester_info = {}

data = input()
while not data == 'end':
    technology =  data.split(' - ')[0]
    courses = data.split(' - ')[1].split(', ')
    semester_info[technology] = semester_info.get(technology, {})
    for course in courses:
        course_name = course.split(':')[0]
        participants = int(course.split(':')[1])
        semester_info[technology][course_name] = semester_info[technology].get(course_name, 0) + participants
    data = input()

sorted_technologies = sorted(semester_info.keys(), key=lambda t: -sum(semester_info[t].values()))
most_popular = sorted_technologies[0]
least_popolar = sorted_technologies[-1]

mp_total_participants = sum([participants for participants in semester_info[most_popular].values()])
lp_total_participants = sum([participants for participants in semester_info[least_popolar].values()])
print(f'Most popular: {most_popular} ({mp_total_participants} participants)\n'
      f'Least popular: {least_popolar} ({lp_total_participants} participants)')


for technology in sorted_technologies:
    courses = semester_info[technology]
    sorted_courses = sorted(courses.items(), key=lambda kvp: -kvp[1])
    tp = sum([tpl[1] for tpl in sorted_courses])
    print(f'{technology} ({tp} participants):')
    for course in sorted_courses:
        print(f'--{course[0]} -> {course[1]}')