def no_of_paint_buckets(height,width,coverage=7):
    area=height*width
    no_of_paint_buckets=round(area/coverage)
    print(f"the area you want to paint is \"{area}\" sq.meters")
    print((f"no.of paint buckets needed to paint is : {no_of_paint_buckets}"))
no_of_paint_buckets(4,6,)
no_of_paint_buckets(7,5,5)
no_of_paint_buckets(9,7,10)