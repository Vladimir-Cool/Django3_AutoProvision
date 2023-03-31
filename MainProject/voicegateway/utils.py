from django.views.generic import View
from django.shortcuts import render, redirect



from .models import TypeGateway, MainGateway


class CreateObjectsMixin(View):
    model_form = None
    templates = None
    redirect_target = None


    def get(self, request):
        form = self.model_form()
        return render(request, self.templates, context={'form': form})


    def post(self, request):
        bound_form = self.model_form(request.POST, request.FILES)

        if bound_form.is_valid():
            new_objects = bound_form.save()
            if self.redirect_target:
                return redirect(self.redirect_target)
            return redirect(new_objects)
        return render(request, self.templates, context={'form': bound_form})






