score = [80,75,90,60,85]
print(score[1:4])
print(sum(score)/len(score))
score.append(95)
print(score)

# idxmin = 0
# for i in range(len(score)):
#     if(score[i]<score[idxmin]):
#         idxmin = i
# score.pop(idxmin)
# print(score)
score.remove(min(score))
print(score)