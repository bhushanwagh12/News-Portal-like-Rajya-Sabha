from django.shortcuts import render

# Create your views here.

# information about parliament
def parliamentInfo(request):
    my_dict={'head_msg':'Parliament Information',
             'sub_msg1':'The essence of these initiatives is aimed at accountability and citizen-centric approach of the Government. The Minister also said that Mobile App was brought by the Government to enable the citizens to file RTI ',
             'sub_msg2':'The Constitution (One Hundred and Twenty-Fourth Amendment) Bill, 2019 was introduced in Lok Sabha by the Minister of Social Justice and Empowerment',
             'sub_msg3':'The Rajya Sabha on Wednesday passed the Motor Vehicles (Amendment) Bill, 2019, to amend the provisions under the Motor Vehicles Act',
             'photo':'parliament.jpg'}
    return render(request,'news.html',context=my_dict)

# information about politics
def politicsInfo(request):
    my_dict={'head_msg':'Politics Information',
             'sub_msg1':'Government to move Ordinance for new law on triple talaq, 3-year jail term for guilty',
             'sub_msg2':'As the demand for a separate north Karnataka state resurfaced, Chief Minister HD Kumaraswamy said on Tuesday, that the state government was considering shifting some government offices to Suvarna Vidhana Soudha in the region, in an attempt to address alleged discrimination.',
             'sub_msg3':'Hundreds of farmers, including the womenfolk, on Sunday staged a protests here against the state governments alleged indifference over ensuring minimum support price for sugarcane and in getting their arrears released from the mill owners',
             'photo':'politics.jpg'}
    return render(request,'politics.html',context=my_dict)
# infromation about sports
def sportsInfo(request):
    my_dict = {'head_msg': 'Sports Information',
               'sub_msg1': 'Michael Phelps makes statement after appearing in court',
               'sub_msg2': 'Usain Bolt enhanced his already legendary Olympic status with an unprecedented third consecutive 100m, 200m and 4x100m triple at Rio 2016',
               'sub_msg3': 'Hima Das, nicknamed the Dhing Express, is an Indian sprint runner from the state of Assam. She holds the current Indian national record in 400 metres with a timing of 50.79 s that she clocked at the 2018 Asian Games in Jakarta, Indonesia',
               'photo': 'phelps.jpg'}
    return render(request, 'sports.html', context=my_dict)


def index(request):
    return render(request, 'index.html')