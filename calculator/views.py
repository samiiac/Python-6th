from django.shortcuts import render
from calculator.models import CalculatorHistory

# Create your views here.


def calcIndex(request):

    context = {}
    data ={}

    if request.method == "POST":
        form_data = request.POST
        number_a = form_data.get("number_a")
        number_b = form_data.get("number_b")
        operation = list(form_data.keys())[-1]
        # breakpoint() to stop the server

        # print(f"a:{number_a} b:{number_b}")

      
        try:
            number_a = float(number_a)
            number_b = float(number_b)
            
            data.update({
                'number_a':number_a,
                'number_b':number_b
            })
            
            action=""
            message=""

            if "add" in operation:
                
                total = number_a + number_b
                action='add'
                message=f"Addition of {number_a} and {number_b} is : {total}"
                
                
            elif "sub" in operation:
                action='sub'
                total = number_a - number_b
                message=f"Subtraction of {number_a} and {number_b} is : {total}" 
                
            elif "multi" in operation:
                action="multi"
                total = number_a * number_b
                message=f"Product of {number_a} and {number_b} is : {total}"
                
                
            elif "div" in operation:
                action='div'
                if number_b == 0:
                    message=f"Denominator must be nonzero!"
                  
                else:
                    total = number_a / number_b
                    message=f"Quotient of {number_a} and {number_b} is : {total}"  
                    
                
            context.update({
                'message' : message
            })
            
            data.update({
                'operation':action,
                'operation_status':'success',
                'result':message
            })
            
            CalculatorHistory.objects.create(**data)
            
        except(ValueError , TypeError):
            context.update({
                'message':'Please enter valid numbers'
            })
            

    return render(request, "calc.html", context)


