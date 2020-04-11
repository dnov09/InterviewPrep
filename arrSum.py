def arraySum(inputs, tests):
    # Write your code here
    # find all possible sums and store in dict

    sumdict={}
    for i in range(len(inputs)):
        for j in range(i,len(inputs)):
            if i == j :
                continue
            else:
                if (inputs[i] + inputs[j]) in sumdict:
                    continue
                else:
                    sumdict[inputs[i]+inputs[j]]=1

    for i in tests:
        if i in sumdict:
            return True
    return False


        