print("Number Pattern")

# decide the row count. (above pattern contains 5 rows )
row = 5
# start: 1
# stop: row+1(range never include stop number in result)
# step: 1
# run loop 5 time
for i in range(1, row + 1, 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("")    