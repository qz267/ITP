//
//  main.cpp
//  testOfCplus
//
//  Created by ZHENG QIN on 4/11/12.
//  Copyright (c) 2012 NYU. All rights reserved.
//

#include <iostream>
#include "test.cpp"

int main (int argc, const char * argv[])
{

    // insert code here...
    Test t = Test();
    int n;
    std::cout<<"please set the number:";
    std::cin>>n;
    t.setnum(n);
    std::cout<<"the Number is:"<<t.rp()<<"/h";
//    std::cout<<"please set the sorce";
//    std::cin>>n;
//    t.
//    std::cout<<""<<t.rp()<<
    
    std::cout << "Hello, World!\n";
    return 0;
}

