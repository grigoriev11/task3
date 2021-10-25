# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

enter_list  =  input ( "Введите список чисел, разделенных пробелом:" ). разделить ()

num_list  = [ int ( i ) для  i  во  введенном_списке ]
max_number  =  num_list [ 0 ]

для  i  в  num_list :
    если  i  >  max_number :
        max_number  =  я
max_number_finish  =  max_number
сумма_  =  0
а  max_number  ! =  0 :
    sum_  =  sum_  +  MAX_NUMBER  %  10
    max_number  =  max_number  //  10
print ( f'На самое большее число по сумме цифр: { max_number_finish } , сумма цифр числа { sum_ } ' )
