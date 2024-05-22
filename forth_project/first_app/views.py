from django.shortcuts import render

def home(request):
    return render(request, './first_app/index.html', {"names":"Samiul","marks":12, "coursces":
        [
            {
            "id": 1,
            "course": "c",
            "teacher": "Rahim"
            },
            {
            "id": 2,
            "course": "c++",
            "teacher": "karim"
            },
            {
            "id": 3,
            "course": "python",
            "teacher": "someone"
            }
        ]})
