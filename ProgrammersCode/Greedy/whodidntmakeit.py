def solution(participant, completion):
    participant.sort()
    completion.sort()
    result = ''
    for i in participant:
        if participant[i] != completion[i]:
            result = participant[i]
            return result