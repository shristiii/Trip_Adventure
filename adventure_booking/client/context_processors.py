from client.models import ClientDetail

def client_detail(request):
    client_details = ClientDetail.objects.all()
    print(client_details)
    return {'client_details':client_details}
