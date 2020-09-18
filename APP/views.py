from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from . models import Car,Bookmark
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,"index.html")
class IndexListView(ListView):
    model = Car
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        if self.request.GET.get('sub')=="true":
            email=self.request.GET.get('email')
            name=self.request.GET.get('name')
            phone=self.request.GET.get('phone')
            check_email=Newsletter.objects.filter(email=email)
            if check_email.exists():
                context['message']=' This Email is Subscribed Already'
            else:
                news=Newsletter.objects.create(email=email,phone=phone,name=name)
                news.save()
                context['message']='Subscribed Successfully'
                fromaddr = "housing-send@advancescholar.com"
                toaddr = email
                subject="Newsletter Subscription"
                msg = MIMEMultipart()
                msg['From'] = fromaddr
                msg['To'] = toaddr
                msg['Subject'] = subject


                body = "You have successfully subscribed to our Newsletter..Look Up our website @ www.afriCar.com.ng and look through our properties"
                msg.attach(MIMEText(body, 'plain'))

                server = smtplib.SMTP('mail.advancescholar.com',  26)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login("housing-send@advancescholar.com", "housing@24hubs.com")
                text = msg.as_string()
                server.sendmail(fromaddr, toaddr, text)
        elif self.request.method == 'POST':
            if self.request.POST.get("login")=="true":
                email = self.request.POST['email']
                password = self.request.POST['password']
                user = auth.authenticate(email=email, password=password)
                if user is not None:
                    auth.login(request, user)
                    context['message']="logged in"
                else:
                    context['message']="invalid login credentials"
        elif self.request.GET.get('third_check')=="three":
            if self.request.user.is_authenticated:
                title=self.request.GET.get('title')
                power=self.request.GET.get('power')
                speed=self.request.GET.get('speed')
                category=self.request.GET.get('category')
                model=self.request.GET.get('model')
                price=self.request.GET.get('price')
                model_year=self.request.GET.get('model_year')
                image=self.request.GET.get('image')
                image_url=image.replace('/media/','')
                transmission=self.request.GET.get('transmission')
                fuel_type=self.request.GET.get('fuel_type')
                condition=self.request.GET.get('condition')
                use_state=self.request.GET.get('use_state')
                book_check=Bookmark.objects.filter(title=title,power=power,speed=speed,category=category,price=price,model_year=model_year,image=image_url,
                transmission=transmission,fuel_type=fuel_type,condition=condition,use_state=use_state,creator=self.request.user)
                if book_check:
                    pass
                else:
                    book=Bookmark.objects.create(title=title,power=power,speed=speed,category=category,price=price,model_year=model_year,image=image_url,
                    transmission=transmission,fuel_type=fuel_type,condition=condition,use_state=use_state,creator=self.request.user)
                    book.save()

        context['cars'] = Car.objects.all()


        return context
class CarDetailView(DetailView):
    model = Car
    template_name = "listing.html"

    def get_object(self, queryset=None):
        global obj
        obj = super(CarDetailView, self).get_object(queryset=queryset)
        print(obj)
        return obj
    def get_context_data(self, **kwargs):
        context = super(CarDetailView, self).get_context_data(**kwargs)

        context['cars'] = Car.objects.all()
        return context

class SearchListView(ListView):
    model = Car
    template_name = "page_featured.html"
    def get_context_data(self, **kwargs):
        context = super(SearchListView, self).get_context_data(**kwargs)
        search=''
        if self.request.GET.get('first_check')=="one":
            first_check="one"
            query = self.request.GET.get('keyword')
            use_state= self.request.GET.get('use_state')
            arrange=self.request.GET.get('arrange')
            category= self.request.GET.get('category')
            if category:
                category= self.request.GET.get('category')
            else:
                category=""
            model= self.request.GET.get('model')
            if model:
                model= self.request.GET.get('model')
            else:
                model=''
            make= self.request.GET.get('make')
            if model:
                make= self.request.GET.get('make')
            else:
                make=''
            year_min=self.request.GET.get('year_min')
            if year_min:
                new_year_min=int(year_min)
            else:
                new_year_min=1950
            year_max=self.request.GET.get('year_max')
            if year_max:
                new_year_max=int(year_max)
            else:
                new_year_max=2020
            price_min=self.request.GET.get('price_min')
            if price_min:
                new_price_min=int(price_min)
            else:
                new_price_min=1000
            price_max=self.request.GET.get('price_max')
            if price_max:
                new_price_max=int(price_max)
            else:
                new_price_max=1000000
            fuel_type=self.request.GET.get('fuel_type')
            if fuel_type:
                fuel_type= self.request.GET.get('fuel_type')
            else:
                fuel_type=''
            condition=self.request.GET.get('condition')
            if condition:
                condition= self.request.GET.get('condition')
            else:
                condition=''
            transmission=self.request.GET.get('transmission')
            if transmission:
                transmission=self.request.GET.get('transmission')
            else:
                transmission=""
            if first_check=="one":
                search = self.model.objects.filter(Q(title__icontains=query),Q(use_state__icontains=use_state),Q(category__icontains=category),Q(fuel_type__icontains=fuel_type),Q(condition__icontains=condition),Q(model__icontains=model), Q(transmission__icontains=transmission),Q(make__icontains=make),Q(model_year__range=(new_year_min, new_year_max)),Q(price__range=(new_price_min, new_price_max)))
                context['search'] = search
            else:
                search = self.model.objects.none()
                context['search'] = search
        elif self.request.GET.get('third_check')=="three":
            if self.request.user.is_authenticated:
                title=self.request.GET.get('title')
                power=self.request.GET.get('power')
                speed=self.request.GET.get('speed')
                category=self.request.GET.get('category')
                model=self.request.GET.get('model')
                price=self.request.GET.get('price')
                model_year=self.request.GET.get('model_year')
                image=self.request.GET.get('image')
                image_url=image.replace('/media/','')
                transmission=self.request.GET.get('transmission')
                fuel_type=self.request.GET.get('fuel_type')
                condition=self.request.GET.get('condition')
                use_state=self.request.GET.get('use_state')
                book_check=Bookmark.objects.filter(title=title,power=power,speed=speed,category=category,price=price,model_year=model_year,image=image_url,
                transmission=transmission,fuel_type=fuel_type,condition=condition,use_state=use_state,creator=self.request.user)
                if book_check:
                    pass
                else:
                    book=Bookmark.objects.create(title=title,power=power,speed=speed,category=category,price=price,model_year=model_year,image=image_url,
                    transmission=transmission,fuel_type=fuel_type,condition=condition,use_state=use_state,creator=self.request.user)
                    book.save()
        if search:
            paginator= Paginator(search,10)
            page_number = self.request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context['page_obj'] = page_obj
        return context

class CategoryListView(ListView):
    model = Car
    template_name = "cars.html"
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        search=''
        if self.request.GET.get('search')=="true":
            first_check="one"
            category=self.request.GET.get("category")
            if first_check=="one":
                search = self.model.objects.filter(category=category)
                context['search'] = search

            else:
                search = self.model.objects.none()
                context['search'] = search
        elif self.request.GET.get('third_check')=="three":
            if self.request.user.is_authenticated:
                title=self.request.GET.get('title')
                power=self.request.GET.get('power')
                speed=self.request.GET.get('speed')
                category=self.request.GET.get('category')
                model=self.request.GET.get('model')
                price=self.request.GET.get('price')
                model_year=self.request.GET.get('model_year')
                image=self.request.GET.get('image')
                image_url=image.replace('/media/','')
                transmission=self.request.GET.get('transmission')
                fuel_type=self.request.GET.get('fuel_type')
                condition=self.request.GET.get('condition')
                use_state=self.request.GET.get('use_state')
                book_check=Bookmark.objects.filter(title=title,power=power,speed=speed,category=category,price=price,model_year=model_year,image=image_url,
                transmission=transmission,fuel_type=fuel_type,condition=condition,use_state=use_state,creator=self.request.user)
                if book_check:
                    pass
                else:
                    book=Bookmark.objects.create(title=title,power=power,speed=speed,category=category,price=price,model_year=model_year,image=image_url,
                    transmission=transmission,fuel_type=fuel_type,condition=condition,use_state=use_state,creator=self.request.user)
                    book.save()
                    context['search']
        if search:
            paginator= Paginator(search,10)
            page_number = self.request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context['page_obj'] = page_obj
        return context

def mylisting(request):
    return render(request,"mylistings.html")

def submit_listing(request):
    return render(request,"mylistings.html")
