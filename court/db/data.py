from court.models import Court

Court.objects.all()

court = Court(courtName='Keelung Municipal Tennis Court', courtType='硬地',locationCity = 'Keelung City')
court.save()

Court.objects.all().values()

Court1 = Court(courtName='Xiao Bitan Tennis Court', courtType='硬地',locationCity = 'New Taipei City')
Court2 = Court(courtName='Taipei Tennis Center', courtType='硬地',locationCity = 'Taipei City')
Court3 = Court(courtName='Fengjia University Tennis Court', courtType='硬地',locationCity = 'Taichung City')
Court4 = Court(courtName='Martyrs\' Shrine Tennis Court', courtType='紅土',locationCity = 'Tainan City')
Court5 = Court(courtName='好草Good Grass', courtType='草地',locationCity = 'kaohsiung city')
Courts_list = [Court1, Court2, Court3, Court4, Court5]
for x in Courts_list:
    x.save()

Court.objects.all().values()