def max_function(marks):
    i=0
    while i<len(marks):
        j=0
        max=0
        while j<len (marks[i]):
            if marks[i][j]>max:
                max=marks[i][j]
            j+=1
        print(max)
        i+=1
marks=[[14, 7, 9],[34, 12, 56, 3],[34, 5, 67]]
max_function(marks)



Points:  back-end work behind any app, programming

