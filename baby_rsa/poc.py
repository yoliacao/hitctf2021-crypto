from Crypto.Util.number import *
from gmpy2 import *
pk = (52, 
47782489586021221729935382562238217213800826152327617948974334325027793433971508995399461776417812670604694882926777607105164020070178881963632306169611641854448509182837621758791538269408388860349616761041456174827996858614494726877767399938809515247000929894281600963992080920650256329287847887064428158469516438206831721224607859023980203694210651902538562842945949404149023836218548894116477022953606370852246884414011363477543284815671096832245521762246149180260936985618856296642080245029837974725521906177900378634071571992373478242159162403228753252168867425697897820696887070051128304178291193132322824455442092893684929701869625045112839344191126228806117685809636908190595562295591835629941512331963039016185366202513504464795106031092314892430859175307526232632986110464780357940552264674214665391043812843917461961230679207586174459563057178720743465356337218948534837994061644332424634750340190113117958830588820626581860957277456320434445207368613679418733984291985618038226928033006640791987978775285182325347153201516936002001839296455263977479446850434913069389565277028444638437387429263495729274142916464752814676819557878779855996225208596159171827854923873570163767937947956753277454486339143489103105750331110111L,
433229619560374735022060612660487139311547277564407316269466855779330930804160973325703376198605206390912154427123102710354958367692760474727012214464298979098489170777185729836132968187705068687678796437447631516334893543456227545790012358063578349956636488453355182971532300478038635153420232589545761194907476691636706445176390661463152150169542241304542401678253873515488446133330974312465916350895130227137954122794991542025930903127027608739905609108321738139103065645651901833223353774916656293079960486497159730921219805951217073283062070931854507016733789164315751827862830668829125950364981217520865411859759718244136420504507997449935455788230060974032741364271601426191469331266168231203426316280988734802654397014768828735251891167507794161264913387252048434549271931367148180980260205843989153008044839641263127846901551223167574691783927938948745126094512037792728067785201012834153473172824948188352810070916677679450209134179624791196123158336411804834221293611075447043002901607162001357780058394706516204775756666576041740010288970758149528406172022049389998133360726123682741312251431519423867620962951022993364287241463507027520966721930799696555390707280246584903566049326608205785466271642132178515338520410658L, 
594494499417894774789048451572687632660208181953899084791149805130704950465573064455173172705283156011806901684972459390817538594318847879599780068410149543731305374894040638491310362570467887919519584736646557258917947483658649575357363123407313011773027073062592473100264464401987309633458687673513776139455296286685115396610808047870099635374955339289799615102534094497730932884838674370338192153202045642565170696704452991192684466848026383861073123033948004049599266417667125680356386669226827901570782628388996520826906941293858994180130505009152517646592286697346622724843482147801718703310671546709185342317509441259927498881276856470161174444209513355803640646947368551446328198695259259829546707119878154837158880677882305548928799964929213106969848547576414765380870575558771867763848114411251654245747231121164090765647221739709450477815688276801154266722035408374135871417564206013020997849375553619152730479571927135850379285559873197371293312934173379820835252091990919727655797413411368987930118553258247264348519581466374312010472449698571319621067244494880512957538208007914329691196084901181642263713183616896210154681618376310287185315262021479758282631576946335858068664109425856174388362174761355148787245515144L, 
261181509476485410165375351178418657075805043256124045823778754055035546150122155335065215645750231604267318872693494310557376958843829685914382636208107544361140482291909865660810395856913449414106045946602124226832733980696161639105193768954092281635195760991693212657816181524313660831938528737461195472275606167593968953647934279724693129491600232382201769523725243272086370087058597321533767924008747705935388941121530345216164771817150616453601212026925759807092457510188966636612860912597984231762129535299227711879953931847880037605415987083573556274570400085013894504645789376654166259691075373526751505971657856429187752015665407876751018316490729668209646098952144838144486106489379202197360745365239628186669447122272538227142855706247593556669905666428363734481409983627496127639634726855140379146669911302677456457202808949896992958886949162850488164457334796828240069980922051762068458877051063958308363343196940785994299643315504146607392461323382470475501119070077564995866998018505817611171892860136485534016608294708527673407517876647349723758712907513973353401204912431800080247493896815299218218930415151745986776831977527196435124521552249406640177674130330651411672455343809240941664288436809369136070604763156723L, 
781980567294866497501123805923409152921571985796778580310714832500106425599168129745704238460330034743315325966148186558555020834861765526689768371880561510063294857161406783415599987595549249742832472894018336008481239463162160596123334637587102639626334613747584469035377788994951080335145295621141303809208401699383140579784234370433212962549701294557490327915345039736785539182810171621358586598828585945914338147070450135377738837775900049262279077924927424572133106317931037834170242253287377939407573458979723688263335125293054004806634691866986695432845509236568546421095177774413671436200824471636980556801370827632298658729537149331589875199074040922783371553748936641151156007453231144303475285524669545469070200964887839003421723671399980708592531935414262678088053843196096190537828523518384368702604524858315737895816793263164649577505835816917629234902199990503712784374018119048109158314524143587749590847895032293396106716513485468884408566836474462501500356497238218550499994067382687458598481617175106389271282319486609800621311007926196777720697327886147764674266204885628982776927834776344964727336572310616726876742447686216871630304048650918084364293803385183867282800430566589645701462385656793820570672943583L)
size = 4096
c0,c1 = (94439884067875866926510480826480805218086956848743547499198006820458557396798764306362789177343865957780128049481100649740991723046823411381255593998762330282701428367295145704749575923764033888430043419432755523895502809914793389377786178823780078298402526077689075100615167801149188073166609798060195606072633000544828049766057724062947725409167355039403877440527580919770561607036599124342541749265192021823491918944278440530549040290346018294412510920437610359378345321588108996817523300112050660236797578506114472897358316471445079369284771733206616722439988368610144077799745808242486800244677553898369876207696781377538070465563883203111584722721805287175889444151342208592141472448213468221732504380079996468560634932304003913239528756529682825338927264423302712140156109639630352986070846491530710979222740690647201189995078959423441714667664068681190006816257273563900319001844315873583504406793282181337548468252678860728542345494826571860793722889527787190697802307747398283993641414712543326007228545296721676768940364724157476527100408795556913732012808496296586935767075610857696900781575977854898411278115773743046743452254128886824788564219765260031723480676483312846917497210349237445933078576069670523680684713623446L, 36397082263544765924779841921119370016762339442058655416586193728619075025998163340396086334077244844310435402140631243689371206933579011146142036715931618067708305508617210563902014072058872403638202493268214994615135134434419245572034705984431586848768861656760831721539666418749603708776469542844144251059399582543923184073020411373179905155719536662312209785364646479188735299232303697790049147771382959302788060004896713986087257232599766636580823138965201801581260077589060485570410897810958498454358737888682940093471597533949463149992040055832220962541050083923086389598838921222167415555331634007862804183991931445726265293675584802614392692457772587297132115782027787479633548163420352103982803350538152059924978489540395956166707435927694988026192837010341182919501051673735679100778154041581361254807291072654267471473503037873994575370262350787611333206450177404857861689910339996980215797433744385047164909022377659304404477322770853683922772248965438499817404000913895236832920522508813098567854697829563333570746651008308539370730448094601234580689549622502198266967939450827346984012446321546195185770288650359658551649011648788273482810013579385313367223458143686448798406205345442061625590854243243883117300950978940L)

# pk = keygen(size)
# print(pk)
g, h, A, B, p, q = pk

k0 = (c1 * invert(c0, p) * invert(pow(h,A, p),p))%p
k1 = invert(B-1, p-1)
y = (pow(c0,B,p)*pow(h,A,p)*invert(c1,p))%p
ee = (0xfaab*B-1)%(p-1)
# print((pow(c0,B,p)*pow(h,A,p)*invert(c1,p))%p==pow(secret,0xfaab*B-1,p))
# print(ee,y,p)
# print(ee)
# print(pow(secret,ee,p)==y)
d0=(invert(3,p-1))
d1=(invert(ee/3/167,p-1))

yy=pow(pow(y,d0,p),d1,p)
print(yy)
print(pow(y,d0,p))
secret = bytes_to_long("HITCTF2021{Numb3r_Th30ry_1s_Funny!}")
print(pow(secret,167,p)==yy)
# c=(c0*pow(k0,invert(k1,p),p))%p
# ee = ((k1+1)*0x10001-k1)%(p-1)
# print(ee,c)
# print(pow(secret,ee,p)==c)
