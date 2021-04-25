import pdb

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.destination_repository as destination_repository
import repositories.user_repository as user_repository
from models.city import City
from models.country import Country
from models.destination import Destination
from models.user import User

user_1 = User('Giuliano', 'Derosas', 'Bali')
user_repository.save(user_1)

country_1 = Country('Thailand')
country_repository.save(country_1)
country_2 = Country('Japan')
country_repository.save(country_2)

city_1 = City(country_1, 'Bangkok')
city_repository.save(city_1)
city_2 = City(country_2, 'Tokyo')
city_repository.save(city_2)

destination_1 = Destination(user_1, country_1, city_1)
destination_repository.save(destination_1)
destination_2 = Destination(user_1, country_2, city_2)
destination_repository.save(destination_2)


# country_1 = Country("Afghanistan")
# country_repository.save(country_1)
# country_2 = Country("Albania")
# country_repository.save(country_2)
# country_3 = Country("Algeria")
# country_repository.save(country_3)
# country_4 = Country("Andorra")
# country_repository.save(country_4)
# country_5 = Country("Angola")
# country_repository.save(country_5)
# country_6 = Country("Antigua and Barbuda")
# country_repository.save(country_6)
# country_7 = Country("Argentina")
# country_repository.save(country_7)
# country_8 = Country("Armenia")
# country_repository.save(country_8)
# country_9 = Country("Australia")
# country_repository.save(country_9)
# country_10 = Country("Austria")
# country_repository.save(country_10)
# country_11 = Country("Azerbaijan")
# country_repository.save(country_11)
# country_12 = Country("Bahamas")
# country_repository.save(country_12)
# country_13 = Country("Bahrain")
# country_repository.save(country_13)
# country_14 = Country("Bangladesh")
# country_repository.save(country_14)
# country_15 = Country("Barbados")
# country_repository.save(country_15)
# country_16 = Country("Belarus")
# country_repository.save(country_16)
# country_17 = Country("Belgium")
# country_repository.save(country_17)
# country_18 = Country("Belize")
# country_repository.save(country_18)
# country_19 = Country("Benin")
# country_repository.save(country_19)
# country_20 = Country("Bhutan")
# country_repository.save(country_20)
# country_21 = Country("Bolivia")
# country_repository.save(country_21)
# country_22 = Country("Bosnia and Herzegovina")
# country_repository.save(country_22)
# country_23 = Country("Botswana")
# country_repository.save(country_23)
# country_24 = Country("Brazil")
# country_repository.save(country_24)
# country_25 = Country("Brunei Darussalam")
# country_repository.save(country_25)
# country_26 = Country("Bulgaria")
# country_repository.save(country_26)
# country_27 = Country("Burkina Faso")
# country_repository.save(country_27)
# country_28 = Country("Burundi")
# country_repository.save(country_28)
# country_29 = Country("Cabo Verde")
# country_repository.save(country_29)
# country_30 = Country("Cambodia")
# country_repository.save(country_30)
# country_31 = Country("Cameroon")
# country_repository.save(country_31)
# country_32 = Country("Canada")
# country_repository.save(country_32)
# country_33 = Country("Central African Republic")
# country_repository.save(country_33)
# country_34 = Country("Chad")
# country_repository.save(country_34)
# country_35 = Country("Chile")
# country_repository.save(country_35)
# country_36 = Country("China")
# country_repository.save(country_36)
# country_37 = Country("Colombia")
# country_repository.save(country_37)
# country_38 = Country("Comoros")
# country_repository.save(country_38)
# country_39 = Country("Congo")
# country_repository.save(country_39)
# country_40 = Country("Congo, Democratic Republic of the")
# country_repository.save(country_40)
# country_41 = Country("Costa Rica")
# country_repository.save(country_41)
# country_42 = Country("Côte d'Ivoire")
# country_repository.save(country_42)
# country_43 = Country("Croatia")
# country_repository.save(country_43)
# country_44 = Country("Cuba")
# country_repository.save(country_44)
# country_45 = Country("Cyprus")
# country_repository.save(country_45)
# country_46 = Country("Czechia")
# country_repository.save(country_46)
# country_47 = Country("Denmark")
# country_repository.save(country_47)
# country_48 = Country("Djibouti")
# country_repository.save(country_48)
# country_49 = Country("Dominica")
# country_repository.save(country_49)
# country_50 = Country("Dominican Republic")
# country_repository.save(country_50)
# country_51 = Country("Ecuador")
# country_repository.save(country_51)
# country_52 = Country("Egypt")
# country_repository.save(country_52)
# country_53 = Country("El Salvador")
# country_repository.save(country_53)
# country_54 = Country("Equatorial Guinea")
# country_repository.save(country_54)
# country_55 = Country("Eritrea")
# country_repository.save(country_55)
# country_56 = Country("Estonia")
# country_repository.save(country_56)
# country_57 = Country("Eswatini")
# country_repository.save(country_57)
# country_58 = Country("Ethiopia")
# country_repository.save(country_58)
# country_59 = Country("Fiji")
# country_repository.save(country_59)
# country_60 = Country("Finland")
# country_repository.save(country_60)
# country_61 = Country("France")
# country_repository.save(country_61)
# country_62 = Country("Gabon")
# country_repository.save(country_62)
# country_63 = Country("Gambia")
# country_repository.save(country_63)
# country_64 = Country("Georgia")
# country_repository.save(country_64)
# country_65 = Country("Germany")
# country_repository.save(country_65)
# country_66 = Country("Ghana")
# country_repository.save(country_66)
# country_67 = Country("Greece")
# country_repository.save(country_67)
# country_68 = Country("Grenada")
# country_repository.save(country_68)
# country_69 = Country("Guatemala")
# country_repository.save(country_69)
# country_70 = Country("Guinea")
# country_repository.save(country_70)
# country_71 = Country("Guinea-Bissau")
# country_repository.save(country_71)
# country_72 = Country("Guyana")
# country_repository.save(country_72)
# country_73 = Country("Haiti")
# country_repository.save(country_73)
# country_74 = Country("Honduras")
# country_repository.save(country_74)
# country_75 = Country("Hungary")
# country_repository.save(country_75)
# country_76 = Country("Iceland")
# country_repository.save(country_76)
# country_77 = Country("India")
# country_repository.save(country_77)
# country_78 = Country("Indonesia")
# country_repository.save(country_78)
# country_79 = Country("Iran (Islamic Republic of)")
# country_repository.save(country_79)
# country_80 = Country("Iraq")
# country_repository.save(country_80)
# country_81 = Country("Ireland")
# country_repository.save(country_81)
# country_82 = Country("Israel")
# country_repository.save(country_82)
# country_83 = Country("Italy")
# country_repository.save(country_83)
# country_84 = Country("Jamaica")
# country_repository.save(country_84)
# country_85 = Country("Japan")
# country_repository.save(country_85)
# country_86 = Country("Jordan")
# country_repository.save(country_86)
# country_87 = Country("Kazakhstan")
# country_repository.save(country_87)
# country_88 = Country("Kenya")
# country_repository.save(country_88)
# country_89 = Country("Kiribati")
# country_repository.save(country_89)
# country_90 = Country("Korea (Democratic People's Republic of)")
# country_repository.save(country_90)
# country_91 = Country("Korea, Republic of")
# country_repository.save(country_91)
# country_92 = Country("Kuwait")
# country_repository.save(country_92)
# country_93 = Country("Kyrgyzstan")
# country_repository.save(country_93)
# country_94 = Country("Lao People's Democratic Republic")
# country_repository.save(country_94)
# country_95 = Country("Latvia")
# country_repository.save(country_95)
# country_96 = Country("Lebanon")
# country_repository.save(country_96)
# country_97 = Country("Lesotho")
# country_repository.save(country_97)
# country_98 = Country("Liberia")
# country_repository.save(country_98)
# country_99 = Country("Libya")
# country_repository.save(country_99)
# country_100 = Country("Liechtenstein")
# country_repository.save(country_100)
# country_101 = Country("Lithuania")
# country_repository.save(country_101)
# country_102 = Country("Luxembourg")
# country_repository.save(country_102)
# country_103 = Country("Madagascar")
# country_repository.save(country_103)
# country_104 = Country("Malawi")
# country_repository.save(country_104)
# country_105 = Country("Malaysia")
# country_repository.save(country_105)
# country_106 = Country("Maldives")
# country_repository.save(country_106)
# country_107 = Country("Mali")
# country_repository.save(country_107)
# country_108 = Country("Malta")
# country_repository.save(country_108)
# country_109 = Country("Marshall Islands")
# country_repository.save(country_109)
# country_110 = Country("Mauritania")
# country_repository.save(country_110)
# country_111 = Country("Mauritius")
# country_repository.save(country_111)
# country_112 = Country("Mexico")
# country_repository.save(country_112)
# country_113 = Country("Micronesia (Federated States of)")
# country_repository.save(country_113)
# country_114 = Country("Moldova, Republic of")
# country_repository.save(country_114)
# country_115 = Country("Monaco")
# country_repository.save(country_115)
# country_116 = Country("Mongolia")
# country_repository.save(country_116)
# country_117 = Country("Montenegro")
# country_repository.save(country_117)
# country_118 = Country("Morocco")
# country_repository.save(country_118)
# country_119 = Country("Mozambique")
# country_repository.save(country_119)
# country_120 = Country("Myanmar")
# country_repository.save(country_120)
# country_121 = Country("Namibia")
# country_repository.save(country_121)
# country_122 = Country("Nauru")
# country_repository.save(country_122)
# country_123 = Country("Nepal")
# country_repository.save(country_123)
# country_124 = Country("Netherlands")
# country_repository.save(country_124)
# country_125 = Country("New Zealand")
# country_repository.save(country_125)
# country_126 = Country("Nicaragua")
# country_repository.save(country_126)
# country_127 = Country("Niger")
# country_repository.save(country_127)
# country_128 = Country("Nigeria")
# country_repository.save(country_128)
# country_129 = Country("North Macedonia")
# country_repository.save(country_129)
# country_130 = Country("Norway")
# country_repository.save(country_130)
# country_131 = Country("Oman")
# country_repository.save(country_131)
# country_132 = Country("Pakistan")
# country_repository.save(country_132)
# country_133 = Country("Palau")
# country_repository.save(country_133)
# country_134 = Country("Panama")
# country_repository.save(country_134)
# country_135 = Country("Papua New Guinea")
# country_repository.save(country_135)
# country_136 = Country("Paraguay")
# country_repository.save(country_136)
# country_137 = Country("Peru")
# country_repository.save(country_137)
# country_138 = Country("Philippines")
# country_repository.save(country_138)
# country_139 = Country("Poland")
# country_repository.save(country_139)
# country_140 = Country("Portugal")
# country_repository.save(country_140)
# country_141 = Country("Qatar")
# country_repository.save(country_141)
# country_142 = Country("Romania")
# country_repository.save(country_142)
# country_143 = Country("Russian Federation")
# country_repository.save(country_143)
# country_144 = Country("Rwanda")
# country_repository.save(country_144)
# country_145 = Country("Saint Kitts and Nevis")
# country_repository.save(country_145)
# country_146 = Country("Saint Lucia")
# country_repository.save(country_146)
# country_147 = Country("Saint Vincent and the Grenadines")
# country_repository.save(country_147)
# country_148 = Country("Samoa")
# country_repository.save(country_148)
# country_149 = Country("San Marino")
# country_repository.save(country_149)
# country_150 = Country("Sao Tome and Principe")
# country_repository.save(country_150)
# country_151 = Country("Saudi Arabia")
# country_repository.save(country_151)
# country_152 = Country("Senegal")
# country_repository.save(country_152)
# country_153 = Country("Serbia")
# country_repository.save(country_153)
# country_154 = Country("Seychelles")
# country_repository.save(country_154)
# country_155 = Country("Sierra Leone")
# country_repository.save(country_155)
# country_156 = Country("Singapore")
# country_repository.save(country_156)
# country_157 = Country("Slovakia")
# country_repository.save(country_157)
# country_158 = Country("Slovenia")
# country_repository.save(country_158)
# country_159 = Country("Solomon Islands")
# country_repository.save(country_159)
# country_160 = Country("Somalia")
# country_repository.save(country_160)
# country_161 = Country("South Africa")
# country_repository.save(country_161)
# country_162 = Country("South Sudan")
# country_repository.save(country_162)
# country_163 = Country("Spain")
# country_repository.save(country_163)
# country_164 = Country("Sri Lanka")
# country_repository.save(country_164)
# country_165 = Country("Sudan")
# country_repository.save(country_165)
# country_166 = Country("Suriname")
# country_repository.save(country_166)
# country_167 = Country("Sweden")
# country_repository.save(country_167)
# country_168 = Country("Switzerland")
# country_repository.save(country_168)
# country_169 = Country("Syrian Arab Republic")
# country_repository.save(country_169)
# country_170 = Country("Tajikistan")
# country_repository.save(country_170)
# country_171 = Country("Tanzania, United Republic of")
# country_repository.save(country_171)
# country_172 = Country("Thailand")
# country_repository.save(country_172)
# country_173 = Country("Timor-Leste")
# country_repository.save(country_173)
# country_174 = Country("Togo")
# country_repository.save(country_174)
# country_175 = Country("Tonga")
# country_repository.save(country_175)
# country_176 = Country("Trinidad and Tobago")
# country_repository.save(country_176)
# country_177 = Country("Tunisia")
# country_repository.save(country_177)
# country_178 = Country("Turkey")
# country_repository.save(country_178)
# country_179 = Country("Turkmenistan")
# country_repository.save(country_179)
# country_180 = Country("Tuvalu")
# country_repository.save(country_180)
# country_181 = Country("Uganda")
# country_repository.save(country_181)
# country_182 = Country("Ukraine")
# country_repository.save(country_182)
# country_183 = Country("United Arab Emirates")
# country_repository.save(country_183)
# country_184 = Country("United Kingdom of Great Britain and Northern Ireland")
# country_repository.save(country_184)
# country_185 = Country("United States of America")
# country_repository.save(country_185)
# country_186 = Country("Uruguay")
# country_repository.save(country_186)
# country_187 = Country("Uzbekistan")
# country_repository.save(country_187)
# country_188 = Country("Vanuatu")
# country_repository.save(country_188)
# country_189 = Country("Venezuela (Bolivarian Republic of)")
# country_repository.save(country_189)
# country_190 = Country("Viet Nam")
# country_repository.save(country_190)
# country_191 = Country("Yemen")
# country_repository.save(country_191)
# country_192 = Country("Zambia")
# country_repository.save(country_192)
# country_193 = Country("Zimbabwe")
# country_repository.save(country_193)


pdb.set_trace()

