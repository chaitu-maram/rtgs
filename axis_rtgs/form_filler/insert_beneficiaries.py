from form_filler.models import AxisBankBeneficiary

def insert_beneficiaries():
    data = [
        {"name":"FORTUNE HOME THEATRE","account_number":"10074125260","bank_name":"IDFC FIRST BANK","bank_address":"KAVVURI HILLS","ifsc_code":"IDFB0080231"},
        {"name":"DECCAN STONE ENTERPRISE","account_number":"80750200000074","bank_name":"BANK OF BARODA","bank_address":"VIKARABAD","ifsc_code":"BARB0VJTAND"},
        {"name":"PERNI RAVI CHANDRA","account_number":"4712128878","bank_name":"KOTAK MAHINDRA BANK","bank_address":"MALKAJGIRI","ifsc_code":"KKBK0007458"},
        {"name":"PERNI RAVI TEJA","account_number":"1461175000000452","bank_name":"KARUR VYSYA BANK","bank_address":"MANIKONDA","ifsc_code":"KVBL0001461"},
        {"name":"NARAYAN R","account_number":"10558721842","bank_name":"STATE BANK OF INDIA","bank_address":"JUBILEE HILLS","ifsc_code":"SBIN0006130"},
        {"name":"SAI KRISHNA TUMMALA","account_number":"96011381717","bank_name":"COSTAL LOCAL AREA BANK","bank_address":"","ifsc_code":"COAS0000001"},
        {"name":"GSVS DURGA PRASAD","account_number":"159866614104","bank_name":"INDUSLAND BANK","bank_address":"TIRUMALGIRI KARKHAANA, SECUNDERABAD","ifsc_code":"INDB0000290"},
        {"name":"SHREE AMBICA ISPAT","account_number":"50200082488687","bank_name":"HDFC BANK","bank_address":"ATTAPUR","ifsc_code":"HDFC0001031"},
        {"name":"SIPUL ENTERPRISES LIMITED","account_number":"41766153778","bank_name":"STATE BANK OF INDIA","bank_address":"HYDERABAD","ifsc_code":"SBIN0010104"},
        {"name":"CH VENKATA NARAYANA","account_number":"31183497783","bank_name":"STATE BANK OF INDIA","bank_address":"KORUKOLLU","ifsc_code":"SBIN0001346"},
        {"name":"SREE SOORYA INFRA ASSET PROJECTS PVT LTD","account_number":"510101006916015","bank_name":"UNION BANK OF INDIA","bank_address":"JUBILEE HILLS","ifsc_code":"UBIN0905917"},
        {"name":"JAKKA ANUPAMA","account_number":"20260548052","bank_name":"STATE BANK OF INDIA","bank_address":"JUBILEE HILLS","ifsc_code":"SBIN0006130"},
        {"name":"GALAXY ENTERPRISES","account_number":"259676747951","bank_name":"INDUSIND BANK","bank_address":"KARMANGHAT","ifsc_code":"INDB0001680"},
        {"name":"DIVYANI STEELS","account_number":"50200004758785","bank_name":"HDFC BANK","bank_address":"PETBASHEERBAD","ifsc_code":"HDFC0000696"},
        {"name":"M-CO STEEL TRADERS","account_number":"120002130681","bank_name":"CANARA BANK","bank_address":"HIMAYAT NAGAR","ifsc_code":"CNRB0003063"},
        {"name":"MD JAVEED","account_number":"867810110015173","bank_name":"BANK OF INDIA","bank_address":"ATTAPUR","ifsc_code":"BKID0008678"},
        {"name":"PONNURU SAI ANAND","account_number":"0142054000005582","bank_name":"SOUTH INDIAN BANK","bank_address":"VIJAYAWADA","ifsc_code":"SIBL0000142"},
        {"name":"SHAIK AKBAR","account_number":"33575832203","bank_name":"STATE BANK OF INDIA","bank_address":"LANGAR HOUSE HYDERABAD","ifsc_code":"SBIN0003609"},
        {"name":"PRASANTH PANDAMANENI","account_number":"024501533806","bank_name":"ICICI BANK","bank_address":"MEHDIPATNAM","ifsc_code":"ICIC0000245"},
        {"name":"HM STEEL","account_number":"510909010253911","bank_name":"CITY UNION BANK LTD","bank_address":"BALANAGAR","ifsc_code":"CIUB0000464"},
        {"name":"JONWAL TRADERS","account_number":"041363400009987","bank_name":"YES BANK","bank_address":"RP ROAD HYDERABAD","ifsc_code":"YESB0000413"},
        {"name":"SHAGANTI RAVI","account_number":"62235097855","bank_name":"STATE BANK OF INDIA","bank_address":"SECRETARIAT","ifsc_code":"SBIN0020077"},
        {"name":"KUNIYIL VIPINANAND","account_number":"110171262298","bank_name":"CANARA BANK","bank_address":"DAMMAIGUDA","ifsc_code":"CNRB0005901"},
        {"name":"SHRADDHA MOTORS","account_number":"125001621293","bank_name":"CANARA BANK","bank_address":"MANIKONDA","ifsc_code":"CNRB0004524"},
        {"name":"PULIGILLA SANDEEP","account_number":"42599563526","bank_name":"STATE BANK OF INDIA","bank_address":"ASWAPURAM","ifsc_code":"SBIN0020566"},
        {"name":"ASHOK KUMAR CHANDA","account_number":"52205874460","bank_name":"STATE BANK OF INDIA","bank_address":"SRI NAGAR COLONY","ifsc_code":"SBIN0021283"},
        {"name":"K AMARENDER REDDY","account_number":"52201602149","bank_name":"STATE BANK OF INDIA","bank_address":"NAKKALA GUTTA","ifsc_code":"SBIN0020150"},
        {"name":"NUNARATH NARESH","account_number":"62415891960","bank_name":"STATE BANK OF INDIA","bank_address":"KESAMUDRAM","ifsc_code":"SBIN0020156"},
        {"name":"LALITA TRAVELS","account_number":"62478125287","bank_name":"STATE BANK OF INDIA","bank_address":"WARANGAL","ifsc_code":"SBIN0020655"},
        {"name":"SRI HANUMAN RESIDENCY","account_number":"41273618577","bank_name":"STATE BANK OF INDIA","bank_address":"MANUGURU","ifsc_code":"SBIN0013325"},
        {"name":"LAVANYA ENTERPRISES","account_number":"50200107952883","bank_name":"HDFC BANK","bank_address":"BEGUMPET","ifsc_code":"HDFC0000621"},
        {"name":"HARE KRISHNA AGENCIES","account_number":"50200107963480","bank_name":"HDFC BANK","bank_address":"BEGUMPET","ifsc_code":"HDFC0000621"},
        {"name":"DASARI ASHOK","account_number":"62108565174","bank_name":"STATE BANK OF INDIA","bank_address":"KESAMUDRAM","ifsc_code":"SBIN0020156"},
        {"name":"HES INFRA PVT LTD","account_number":"527605010040540","bank_name":"UNION BANK OF INDIA","bank_address":"MID CORPORATE BRANCH HYDERABAD","ifsc_code":"UBIN0577901"},
        {"name":"AMRUTHA AGENCY","account_number":"085311100000159","bank_name":"UNION BANK OF INDIA","bank_address":"MANUGURU","ifsc_code":"UBIN0808539"},
        {"name":"U SRINIVAS RAO","account_number":"62043266415","bank_name":"STATE BANK OF INDIA","bank_address":"MANUGURU","ifsc_code":"SBIN0020514"},
        {"name":"BIKKASANI VENKATESWARA RAO","account_number":"62401522975","bank_name":"STATE BANK OF INDIA","bank_address":"BURGHANPHAD","ifsc_code":"SBIN0020168"},
        {"name":"CHINTHALA KRISHNA PRASAD","account_number":"62334626186","bank_name":"STATE BANK OF INDIA","bank_address":"MANUGURU","ifsc_code":"SBIN0020514"},
        {"name":"SANGANAMONI BALARAJU","account_number":"50100163305183","bank_name":"HDFC","bank_address":"NAGARKURNOOL","ifsc_code":"HDFC0004747"},
        {"name":"ELITE CEMENTS","account_number":"0477360000000997","bank_name":"DBS","bank_address":"MEHDIPATNAM","ifsc_code":"DBSS0IN0477"},
        {"name":"VALLABOINA RAMBABU","account_number":"62380329563","bank_name":"STATE BANK OF INDIA","bank_address":"MANUGURU","ifsc_code":"SBIN0020514"},
        {"name":"BALAJI STEEL AND CEMENT TRADERS","account_number":"1467135000010397","bank_name":"KARUR VYSYA BANK","bank_address":"KUKATPALLY","ifsc_code":"KVBL0001467"},
        {"name":"SRI RAMA SAI RAGHAVA OIL","account_number":"41039423212","bank_name":"STATE BANK OF INDIA","bank_address":"ASWARAPURAM","ifsc_code":"SBIN0020566"},
        {"name":"CHIRUMAMILA V LAKSHMI SANDEEP","account_number":"229711010000048","bank_name":"UNION BANK OF INDIA","bank_address":"VATSAVAI","ifsc_code":"UBIN0822973"},
        {"name":"NANDYALA PRAKASH REDDY","account_number":"36862200044766","bank_name":"CANARA BANK","bank_address":"KAKARLA","ifsc_code":"CNRB0013686"},
        {"name":"TEMPLE CROPS AND CULTIVATORS PVT LTD","account_number":"560381003316693","bank_name":"UNION BANK OF INDIA","bank_address":"FILM NAGAR","ifsc_code":"UBIN0910520"},
        {"name":"UPPALAIAH","account_number":"240001001238966","bank_name":"CITY UNION BANK","bank_address":"KARIM NAGAR","ifsc_code":"CIUB0000240"},
        {"name":"K SRINIVASULU","account_number":"50100620908660","bank_name":"HDFC BANK","bank_address":"PODILI","ifsc_code":"HDFC0003050"},
        {"name":"PRUDHVI RAKESH","account_number":"82358100000596","bank_name":"BANK OF BARODA","bank_address":"PODILI","ifsc_code":"BARB0VJPODI"},
        {"name":"VELUGU VENKATA RAO","account_number":"1422166000019820","bank_name":"KARUR VYSYA BANK","bank_address":"ONGOLE","ifsc_code":"KVBL0001422"},
        {"name":"G KOTI REDDY","account_number":"91197758959","bank_name":"ANDHRA PRAGATHI GRAMEENA BANK","bank_address":"CHIMAKURTHI","ifsc_code":"APGB0005085"},
        {"name":"T J LAZARU","account_number":"4853155000018934","bank_name":"KARUR VYSYA BANK","bank_address":"BUDAWADA","ifsc_code":"KVBL0004853"},
        {"name":"KATAMREDDY RAMANJANEYAREDDY","account_number":"263810100037153","bank_name":"UNION BANK OF INDIA","bank_address":"KONDAPI","ifsc_code":"UBIN0826383"},
        {"name":"KOLLI MANIKANTA","account_number":"40903998742","bank_name":"STATE BANK OF INDIA","bank_address":"JUWIGUNTA PRAKASAM","ifsc_code":"SBIN0007822"},
        {"name":"PINNIKA EDUKONDALU","account_number":"91013109676","bank_name":"ANDHRA PRAGATHI GRAMEENA BANK","bank_address":"BODIKURAPDU","ifsc_code":"APGB0005080"},
        {"name":"DUGGIRALA AJAY KUMAR","account_number":"036002000003348","bank_name":"INDIAN OVERSEAS BANK","bank_address":"ONGOLE","ifsc_code":"IOBA0000360"},
        {"name":"D NARSIMHA RAO","account_number":"62190982451","bank_name":"STATE BANK OF INDIA","bank_address":"MANUGURU","ifsc_code":"SBIN0020514"},
        {"name":"PERNI RAVI TEJA","account_number":"40504974643","bank_name":"STATE BANK OF INDIA","bank_address":"FILM NAGAR HYDERABAD","ifsc_code":"SBIN0006130"},
        {"name":"VENKATESWARULU MALEPATI","account_number":"007505500801","bank_name":"ICICI BANK","bank_address":"S R NAGAR","ifsc_code":"ICIC0000075"},
        {"name":"NEXT MOVE EXPORTS AND IMPORTS","account_number":"059121010000064","bank_name":"UNION BANK OF INDIA","bank_address":"JUBILEE HILLS HYDERABAD","ifsc_code":"UBIN0905971"},
        {"name":"SAMSARAGRO INFRA FOOD AND ENERGY SAFE","account_number":"50200105252960","bank_name":"HDFC BANK","bank_address":"MANUGURU","ifsc_code":"HDFC0006462"},
        {"name":"SREE SOORYA INFRA ASSET PROJECTS PVT LTD","account_number":"4712098416","bank_name":"KOTAK MAHINDRA BANK","bank_address":"JUBILEE HILLS HYDERABAD","ifsc_code":"KKBK0007479"},
        {"name":"BANGARI SURESH","account_number":"20117685879","bank_name":"STATE BANK OF INDIA","bank_address":"FILM NAGAR HYDERABAD","ifsc_code":"SBIN0006130"},
        {"name":"PERNI VIJAYA LAKSHMI","account_number":"520101012663561","bank_name":"UNION BANK OF INDIA","bank_address":"FILM NAGAR HYDERABAD","ifsc_code":"UBIN0910520"},
        {"name":"PERNI RAVI TEJA","account_number":"510101000679215","bank_name":"UNION BANK OF INDIA","bank_address":"FILM NAGAR HYDERABAD","ifsc_code":"UBIN0910520"},
        {"name":"ACE ENTERPRISES","account_number":"007001200016041","bank_name":"MAHESH CO-OPERATIVE URBAN BANK","bank_address":"MG ROAD SECUNDERABAD","ifsc_code":"APMC0000007"},
        {"name":"CHIPURLA MADHU LATHA","account_number":"41637225336","bank_name":"STATE BANK OF INDIA","bank_address":"JUBILEE HILLS","ifsc_code":"SBIN0006130"},
        {"name":"SAI BALAJI DEVELOPERS","account_number":"50200017303375","bank_name":"HDFC BANK","bank_address":"SHADNAGAR","ifsc_code":"HDFC0004330"},
    ]

    # ✅ Clear old data (optional)
    AxisBankBeneficiary.objects.filter(unique_code="978B25").delete()

    # ✅ Create objects for bulk insert
    objs = [AxisBankBeneficiary(unique_code="978B25", **item) for item in data]

    # ✅ Insert all at once
    AxisBankBeneficiary.objects.bulk_create(objs)

    print(f"✅ Inserted {len(objs)} beneficiary records successfully!")

# Allow running directly
if __name__ == "__main__":
    insert_beneficiaries()
