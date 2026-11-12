from django.shortcuts import render

def calculate_churn_rate(request):
    context = {}
    
    if request.method == "POST":
        initial_str = request.POST.get("Initialcust", "0")
        present_str = request.POST.get("Presentcust", "0")
        
        Initialcust = int(initial_str) if initial_str else 0
        Presentcust = int(present_str) if present_str else 0
        print("Initial Customer:",Initialcust)
        print("Present Customer:",Presentcust)
        
        if Initialcust > 0:
            churn_rate = ((Initialcust - Presentcust) / Initialcust) * 100
        else:
            churn_rate = 0
            
    
        print("Calculated Churn Rate:", round(churn_rate, 2), "%")
            
        context = {
            "Initialcust": Initialcust,
            "Presentcust": Presentcust,
            "churn_rate": round(churn_rate, 2),
        }
            
    return render(request, "myapp/math.html", context)