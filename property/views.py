from django.shortcuts import render, redirect
from .forms import PropertyForm, UnitForm, TenantForm, RentalInformationForm
from django.shortcuts import render, get_object_or_404
from .models import Property
from .models import Property, Unit, Tenant, RentalInformation
from .forms import UnitForm

def home(request):
    property = Property.objects.all()

    context = {
        'property':property
    }
    return render(request,'home.html', context)

def property_create_with_unit(request):
    if request.method == 'POST':
        property_form = PropertyForm(request.POST)
        unit_form = UnitForm(request.POST)

        if property_form.is_valid() and unit_form.is_valid():
            property_instance = property_form.save()

            unit_instance = unit_form.save(commit=False)
            unit_instance.property = property_instance
            unit_instance.save()

            return redirect('home') 

    else:
        property_form = PropertyForm()
        unit_form = UnitForm()

    context={
        'property_form': property_form,
        'unit_form': unit_form
        }

    return render(request, 'create_prop_with_unit.html', context)

def property_units_list(request, property_id):
    property_instance = get_object_or_404(Property, id=property_id)
    units = property_instance.units.all()
    form = UnitForm()

    context = {
        'property_instance': property_instance,
        'units': units,
        'form': form
        }
    return render(request, 'unit.html', context)



# Create View
def unit_create(request,property_id):
    property_instance = get_object_or_404(Property, pk=property_id)
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            unit_instance = form.save(commit=False)
            unit_instance.property = property_instance
            unit_instance.save()

            return redirect('property_units', property_id=property_instance.id)
    else:
        return redirect('property_units', property_id=property_instance.id)


# Update View
def unit_update(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    if request.method == 'POST':
        form = UnitForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect('property_units', property_id=unit.property.id)
    else:
        form = UnitForm(instance=unit)
    return render(request, 'unit_form.html', {'form': form})

# Delete View
def unit_delete(request, pk):
    unit = get_object_or_404(Unit, pk=pk)
    unit.delete()
    return redirect('property_units', property_id=unit.property.id)


""" create Tenant along with rental details"""

def create_tenant(request):
    if request.method == 'POST':
        tenant_form = TenantForm(request.POST, request.FILES, prefix='tenant')
        rental_info_form = RentalInformationForm(request.POST, prefix='rental')

        if tenant_form.is_valid() and rental_info_form.is_valid():

            tenant_instance = tenant_form.save()

            rental_info_instance = rental_info_form.save(commit=False)
            rental_info_instance.tenant = tenant_instance
            rental_info_instance.save()

            return redirect('tenant_list')

    else:

        tenant_form = TenantForm(prefix='tenant')
        rental_info_form = RentalInformationForm(prefix='rental')

    return render(request, 'create_tenant.html', {
        'tenant_form': tenant_form,
        'rental_info_form': rental_info_form,
    })

def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenant_list.html', {'tenants': tenants})

def tenant_detail(request, pk):
    tenant = get_object_or_404(Tenant, id=pk)
    rental_info = RentalInformation.objects.select_related('unit__property').filter(tenant=tenant)

    unit_details = rental_info.first().unit if rental_info else None
    property_details = unit_details.property if unit_details else None

    return render(request, 'tenant_detail.html', {
        'tenant': tenant,
        'rental_info': rental_info,
        'unit_details': unit_details,
        'property_details': property_details,
    })