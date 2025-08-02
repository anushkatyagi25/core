from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    peoples=[
        {'name':'Abhishek Gupta','age':26},
        {'name':'Rohan Sharma','age':23},
        {'name':'Vicky Kaushal','age':17},
        {'name':'Deepanshu Chaudhary','age':16},
        {'name':'Sandeep','age':63}
    ]
    
    text="""Lorem ipsum dolor sit, amet consectetur adipisicing elit. Dolor voluptatem tenetur minus qui nobis quis doloremque enim delectus repellendus iste dicta vero neque in iusto, illo praesentium consequatur, facere necessitatibus aut ducimus aperiam mollitia sed temporibus obcaecati. Ad ea ut praesentium non repellat eos, vero dolore unde, aliquam modi minima. Deserunt molestiae vitae minus et, consequuntur dolorem praesentium ex iste esse mollitia voluptatem possimus eligendi maxime quod laudantium vel maiores quibusdam, in facere porro. Molestias minus explicabo laudantium. Qui, iure quod. Impedit, sunt amet labore beatae necessitatibus, architecto voluptatem sit temporibus rerum alias doloremque ab, magnam commodi! Placeat, assumenda aliquam?"""
    vegetables=['Pumpkin','Tomato','Potato']
    return render(request,"index.html",context={'page':'Home','peoples':peoples,'text':text,'vegetables':vegetables})

def success_page(request1):
    print("*"*10)
    return HttpResponse("<h1>Hey this is a success port")

def about(request):
    context={'page':'About'}
    return render(request,"about.html",context)

def contact(request):
    context={'page':'Contact'}
    return render(request,"contact.html",context)