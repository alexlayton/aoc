def run(x, n):
    x = x.split("\n")
    x = list(map(int, x))
    print(xmas(x, n)[0])
    print(xmas2(x, n))


def xmas(x, n):
    for i in range(n, len(x)):
        if not is_valid(x[i], x[i - n : i]):
            return x[i], i


def xmas2(x, n):
    y, idx = xmas(x, n)
    start, end, curr = 0, 1, x[0]
    while start <= idx:
        while curr > y and start < end - 1:
            curr -= x[start]
            start += 1
        if curr == y:
            return min(x[start:end]) + max(x[start:end])
        if end < idx:
            curr += x[end]
        end += 1


def is_valid(x, values):
    values_set = set(values)
    for y in values:
        if x - y in values_set:
            return True
    return False


if __name__ == "__main__":
    x = """1
30
41
23
5
4
21
33
19
32
24
35
6
31
14
26
47
13
7
49
40
17
9
16
18
8
37
11
10
12
15
34
67
20
56
62
19
21
22
23
32
26
24
25
48
53
27
64
28
52
18
30
29
31
92
37
38
39
50
41
42
44
40
49
70
58
55
88
43
46
71
45
87
57
47
48
59
66
75
84
76
90
83
129
92
82
85
106
204
89
91
125
103
95
149
104
93
105
182
107
114
134
141
158
159
161
199
165
171
177
189
174
180
358
184
207
347
188
496
252
197
275
212
293
221
248
292
362
317
320
326
339
349
559
357
354
385
364
409
643
395
400
433
418
449
546
460
504
469
513
540
641
682
738
646
931
688
706
711
894
718
1183
759
795
1326
813
818
851
867
909
929
964
973
982
1181
1186
1287
1328
1334
1352
1424
1394
1600
1429
1662
1893
1554
1759
1608
1664
2628
2529
1815
1776
1838
1902
1937
1955
2163
3166
2473
2722
2763
2686
4583
2818
5121
2983
3322
3892
5215
3162
4137
3272
3440
5377
9269
6423
5485
3740
6578
10068
4118
4636
5159
5848
5958
5669
5504
7062
5801
6305
9740
8029
12221
6434
11470
6712
9244
9863
7858
8376
8754
15869
8899
15541
9277
9622
9795
11462
11173
11938
11305
11809
12106
12235
21053
15678
13146
32523
18650
14570
20611
21005
16612
16234
17130
17653
21431
18176
27453
18899
19417
20968
39607
22478
23114
23411
23915
33203
33854
37075
27716
29380
31700
30804
32223
34265
32846
46525
60184
34783
35829
52620
37593
38316
42013
40385
58180
45592
45889
53918
47326
60919
59939
57096
58520
75269
68397
62504
63027
92414
67111
67629
70612
72376
92963
93005
75909
104517
99807
139009
85977
91481
92918
230490
108245
107265
115616
117035
119600
121024
125531
129615
133639
159525
138241
134740
191288
142988
180426
161886
175716
216842
178895
211508
177458
296042
184399
200183
226865
413077
263772
232651
301247
267856
246555
255146
272603
714324
326028
354611
296626
569103
304874
339344
353174
356353
428350
361857
450061
459516
490637
446738
510327
473420
518918
551772
533898
803091
501701
527749
560020
577477
601500
622654
652979
751612
718210
644218
692518
826594
784703
1001833
821373
1253152
992338
1477221
1344723
975121
1050897
1319710
1154680
1194219
1029450
1061721
1087769
1212999
1178977
1224154
1410728
1297197
1336736
2472449
1428921
1976053
1606076
2583601
1976954
2407479
1967459
2004571
2036842
2026018
2062890
2348094
2333657
2091171
3092340
2117219
2274720
2510196
2391976
4551060
3334039
2942812
4383532
2765657
3034997
3396380
4536214
3573535
3944413
3972030
4374938
4099732
4627415
4608377
4117189
4154061
4424828
4208390
5060031
4391939
8942999
5977809
8491671
5334788
8808360
5708469
7418529
5800654
9709726
6431377
6969915
8061602
9949839
8044145
9019354
8216921
9159763
8271250
8509128
8325579
8362451
8600329
11312597
9451970
9726727
14609014
13396390
11043257
13401292
15031517
13126998
15241165
12232031
14475522
16315395
15014060
16369724
16261066
17496115
17619683
16488171
17522214
16596829
16688030
16962780
31571794
18052299
35115798
19178697
29623074
34582463
23275288
27263548
25359029
29754245
32949096
26707553
28493097
29489582
33003425
31502231
32630790
47250360
33085000
33176201
33284859
33559609
57989819
43670333
52078578
45315847
37230996
53971101
87056101
53029533
80571675
64587231
52066582
90620609
55200650
56197135
57982679
61578097
62120372
64787090
66261201
76755333
66369859
66461060
97763432
70790605
122769769
80901329
82546843
89297578
108263717
90260529
162550522
110049261
105096115
107267232
113644679
113183329
111397785
200695363
114179814
119560776
123698469
180441015
202942257
105950735
143216393
137251665
381136378
151691934
153337448
163448172
186852064
223232590
179558107
203443858
195356644
211046850
257642669
285537130
213217967
217348520
250434994
220130549
317692680
327142327
249167128
229649204
243202400
259288183
269398907
280468058
463652961
305029382
315140106
348694092
343006279
501992170
374914751
383001965
508455311
406403494
424264817
430566487
749190091
602294462
446997724
712820089
449779753
472851604
478816332
667467217
488937387
942469293
528687090
1042381968
623474337
987271643
755097586
690054857
691700371
717921030
757916716
939021798
922631357
830668311
854831304
1114464941
1357392048
1269761679
896777477
919849328
1164551975
928596085
1168871189
967753719
1359355401
1017624477
1448536418
1152161427
1685499615
1313529194
1381755228
1407975887
1409621401
1449617087
1475837746
1588585027
1753299668
1727445788
1750517639
2256132878
1848445413
1816626805
2767331288
2072010755
1887603047
2310351313
3479222502
2560137314
3437030440
2169785904
2331153671
3132272867
2533916655
3705749965
3337220134
2789731115
2817597288
4480137217
2925454833
3064422773
3316030815
3923085572
3477963427
3959613802
4072759683
3665072218
3704229852
4057388951
4197954360
4218756718
7024036575
7551982185
5302058771
4500939575
5234208677
4865070326
6752673373
9802998346
6295560715
5607328403
8550239492
5743052121
5989877606
9815811804
6380453588
6793994242
7550723110
7143035645
7369302070
7722461169
7761618803
12631364978
9432163037
14668068672
11617743699
10099279003
12234372396
14540117098
13664862785
10472398729
10608122447
11350380524
13293775231
11597206009
11732929727
12123505709
12370331194
14920025180
16575198682
13174447830
14344717352
14865496814
14904654448
15091763239
17860897806
17193781840
21165092764
24644155755
20707401450
25699885686
20571677732
23646846559
21080521176
41837937595
21822779253
21958502971
26652954907
23330135736
23720711718
23856435436
31479853130
25544779024
27519165182
36030589578
34339540594
29249371800
29770151262
29996417687
32285545079
53416997821
37765459572
41279079182
46116456756
41652198908
42530180703
47367558277
42903300429
44410656912
43781282224
45152914989
45288638707
47050847454
47186571172
71300447406
49401214460
53063944206
55314930286
56768536982
70901570708
77047265141
71275496869
72300331965
62281962766
121457922053
85433481132
79044538754
83809259885
84555499337
95967244635
122335903848
86684582653
87313957341
130465864877
100250515378
90441553696
92339486161
94237418626
96587785632
102465158666
104716144746
108378874492
112083467268
146837462103
139329227907
133557459635
183901742973
134582294731
141326501520
182021266764
162853798639
180397045517
168364759222
191400727399
173998539994
184678972322
177126136349
187029339328
182781039857
225896945796
186576904787
228819713357
190825204258
302183026546
207181303412
213095019238
372846471022
323347768284
268139754366
272886687542
304180300159
381459778460
382225931657
309691260742
343250844156
358677512316
408677985653
691917192399
572284982718
356779579851
389962343269
490757204946
556345863394
369357944644
377402109045
679585135591
398006507670
403920223496
660959880010
420276322650
481234773604
933846567552
626817266682
541026441908
577066987701
728035456960
652942104898
1110261388617
754786087521
746741923120
715457092167
787968850939
726137524495
746760053689
1119377315663
767364452314
824196546146
773278168140
1208245173589
775408616715
818282830320
997343310351
885154997100
1628521496239
901511096254
1606251681259
1167843708590
1445100097002
1493501976809
1477138651044
1420306557212
1426220273038
1441594616662
1462199015287
1462217145856
1472897578184
2218378265142
1514124506003
2201628889753
1591560998460
1593691447035
3663478362144
1548686784855
2871320370040
1660563613815
2424534511579
1786666093354
2052998705690
2363728242110
2630060854446
2594063981628
3678767540797
2955719122665
2899117851222
2914492194846
4085098125394
2867814889700
6984215976616
4016095510039
5069443779453
2987022084187
4144185360449
4462881368500
5529178705668
4221621852906
6550087910837
3209250398670
4024291855925
4528378503515
5508556176474
8278694178123
7072120209581
7233542254595
5224124836074
5493181832850
6915213361261
8101193635433
6108368249892
5766932740922
5782307084546
5854836973887
8552670359440
6196272482857
7003117594226
13015551727940
7011313940112
7353435759119
7430872251576
10383215477402
7737628902185
8702432231520
11637144058433
11761920758110
15193907539384
11689454315707
10717306668924
10991057576996
17386333071628
11006431920620
11260114573772
11549239825468
11621769714809
11875300990814
11963205223779
17114951547659
18990579817552
13549708241976
26421452069128
14356553353345
14364749699231
14442186191688
16055867990639
15168501153761
27131706377540
16440061133705
19708864152140
21708364245920
22540297402464
21723738589544
22954262800775
21977421242696
21997489497616
28721303052576
22266546494392
35527129484672
23171009540277
36342170941927
23838506214593
30804810832936
27906261595321
28798739545033
30796614487050
28806935890919
36064917599265
29533250852992
29610687345449
51877233839841
36892239743305
38980358536169
38163799723249
41417228398060
45148430782973
43701159832240
49883682838017
43974910740312
50718792550192
44264035992008
59365635699265
45437556034669
51077271135598
52781696885726
51744767809914
52637245759626
56705001140354
66861532086315
57605675435952
73585598085761
81444181650545
96338405591866
97182323844583"""
    run(x, 25)
