# # 1
# def selection_sort(seq: list) -> list:
    
#     for x in range(len(seq)):
#         for y in range(len(seq)):
#             if seq[y] > seq[x]:
#                 seq[x], seq[y] = seq[y], seq[x]

#     return seq

# print(selection_sort([5, 1, 3, 5, 4, 6, 8]))

#2
def insertion_sort(seq: list) -> list:


    for x in range(len(seq) - 1):
        print(seq[x])


        y = x - 1
        while seq[x] <= seq[y] and len(seq) <= y:
            seq[y + 1], seq[y] = seq[y], seq[y +1 ]
            y -= 1
        

    print(seq)

print(insertion_sort([5, 1, 3, 5, 4, 6, 8]))
