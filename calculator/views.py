from django.shortcuts import render

# Create your views here.


def calcIndex(request):
    # result = None
    # number_a = ''
    # number_b = ''

    # if request.method == 'POST':
    #     try:
    #         number_a = float(request.POST.get('number_a',0))
    #         number_b = float(request.POST.get('number_b',0))
    #         result = number_a + number_b
    #     except(ValueError,TypeError):
    #         result = 'Invalid input'
    #     return render(request,'calc.html',{ 'sum':result})

    # return render(request,'calc.html')

    context = {}

    if request.method == "POST":
        form_data = request.POST
        number_a = form_data.get("number_a")
        number_b = form_data.get("number_b")
        operation = list(form_data.keys())[-1]
        # breakpoint() to stop the server

        # print(f"a:{number_a} b:{number_b}")

        if number_a.isnumeric() and number_b.isnumeric():
            number_a = float(number_a)
            number_b = float(number_b)

            if "add" in operation:
                total = number_a + number_b
                context.update(
                    message=f"Addition of {number_a} and {number_b} is : {total}"
                )
            elif "sub" in operation:
                total = number_a - number_b
                context.update(
                    message=f"Subtraction of {number_a} and {number_b} is : {total}"
                )
            elif "multi" in operation:
                total = number_a * number_b
                context.update(
                    message=f"Product of {number_a} and {number_b} is : {total}"
                )
            elif "div" in operation:
                if number_b == 0:
                    context.update(
                    message=f"Denominator must be nonzero!"
                )
                else:
                    total = number_a / number_b
                    context.update(
                    message=f"Quotient of {number_a} and {number_b} is : {total}"
                )

        else:
            context.update(message="You need to pass numeric values!")
    return render(request, "calc.html", context)
