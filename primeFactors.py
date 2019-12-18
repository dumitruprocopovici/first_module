# def primeFactors(number):
#     count = 1
#     start_at = 2
#     result = ''
#     while number > 1:
#         for i in range(start_at, number // 2):
#             if number % i == 0:
#                 result += '(' + str(i)
#                 number = number // i
#                 while number % i == 0:
#                     count += 1
#                     number = number // i
#                 if count == 1:
#                     result += ')'
#                 else:
#                     result += '**' + str(count) + ')'
#                     count = 1
#                 start_at = i
#             continue
#     return result


# print(primeFactors(7775460))

