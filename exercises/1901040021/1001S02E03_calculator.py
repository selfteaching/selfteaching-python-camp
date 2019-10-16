def jjcc(fuhao):
    one=input("the first numble:");
    two=input("the second numble");
    if(fuhao=="+"):
       result=float(one)+float(two);
    elif(fuhao=="-"):
        result=float(one)-float(two);
    elif(fuhao=="*"):
        result=float(one)*float(two);
    else:
        if(float(two)==0):
          result=0;
        else:
            result=float(one)/float(two);
    print("the result is",result);

    return result;

jjcc("/");





