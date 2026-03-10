from dataclasses import dataclass
from typing import Iterable
from uuid import UUID


@dataclass(frozen=True, slots=True)
class Location:
    id: str
    name: str

    def __str__(self) -> str:
        return self.id


class Locations:
    ACCRINGTON = Location(
        id="0e32cd63-519f-4486-8911-a1f3fa978a52",
        name="Accrington",
    )

    ALTRINCHAM = Location(
        id="951ce87c-b929-4e22-b303-5df4d8dfd22e",
        name="Altrincham",
    )

    ASHFORD = Location(
        id="df51d49c-ad25-43f3-9525-fe06358a0853",
        name="Ashford",
    )

    AYLESBURY = Location(
        id="22feef84-59ff-4275-a276-cfa5d1364f43",
        name="Aylesbury",
    )

    AYR = Location(
        id="d75c9dd2-dfd1-435d-81fd-d9e49bb7dbe2",
        name="Ayr",
    )

    BARNSLEY = Location(
        id="22d6942f-534b-4a20-9d67-9ace58de081e",
        name="Barnsley",
    )

    BARROW_IN_FURNESS = Location(
        id="bd42b165-aab7-4a11-ab5b-59e1fffd56db",
        name="Barrow-in-Furness",
    )

    BASILDON = Location(
        id="ce412dd6-3865-4633-b131-be69954ef15f",
        name="Basildon",
    )

    BASINGSTOKE = Location(
        id="14b496fd-726c-4a7a-a940-1cc009ff3329",
        name="Basingstoke",
    )

    BATH_CITY = Location(
        id="e4ec9448-2949-4907-a65e-f510f5f9981d",
        name="Bath City",
    )

    BEDFORD = Location(
        id="ac3a5936-ed3f-4197-875f-0dc887349675",
        name="Bedford",
    )

    BEVERLEY = Location(
        id="d7e0c17b-8e20-4553-8038-d07964a328db",
        name="Beverley",
    )

    BEXLEYHEATH = Location(
        id="c7d18b98-aea5-4a01-ba56-cf826d06522d",
        name="Bexleyheath",
    )

    BIRMINGHAM_BROAD_STREET = Location(
        id="21fb9bfb-9b85-44f9-960b-40fe51465b62",
        name="Birmingham Broad Street",
    )

    BIRMINGHAM_CITY_CENTRE = Location(
        id="45d2fadb-a5e5-41b6-887b-ba22985fb9c2",
        name="Birmingham City Centre",
    )

    BIRMINGHAM_DIGBETH = Location(
        id="265ba3de-e1c5-42ad-9d29-89e77ba78692",
        name="Birmingham Digbeth",
    )

    BIRMINGHAM_HAGLEY_ROAD = Location(
        id="02179a3b-258e-4c7f-a164-d97000e3a2a4",
        name="Birmingham Hagley Road",
    )

    BIRMINGHAM_KINGS_HEATH = Location(
        id="6b536fdb-1829-4dab-96ee-7e82fe2f19e4",
        name="Birmingham Kings Heath",
    )

    BIRMINGHAM_KINGSBURY_ROAD = Location(
        id="9c3cbcfc-ec4b-4d55-8ef8-941c4b6b817d",
        name="Birmingham Kingsbury Road",
    )

    BIRMINGHAM_PERRY_BARR = Location(
        id="8f83e988-abef-4e90-b0e2-5d850b173453",
        name="Birmingham Perry Barr",
    )

    BIRMINGHAM_SELLY_OAK = Location(
        id="e289f66c-7b60-4167-9d21-b8f774c3a7bc",
        name="Birmingham Selly Oak",
    )

    BIRMINGHAM_SHELDON = Location(
        id="dddf40b6-1340-4a91-bf4e-a78470e14355",
        name="Birmingham Sheldon",
    )

    BIRMINGHAM_STECHFORD = Location(
        id="6b6414b0-034b-4ae1-b8e1-ac056cd2dbc9",
        name="Birmingham Stechford",
    )

    BLACKPOOL = Location(
        id="186a9f71-d9a8-41f1-8f36-697a5ab4bfa8",
        name="Blackpool",
    )

    BOLTON = Location(
        id="c52f363d-91db-4e6e-8339-9642d3e4a4b6",
        name="Bolton",
    )

    BOURNEMOUTH = Location(
        id="f512e501-1036-4ab7-9edd-3a9f764fcf2a",
        name="Bournemouth",
    )

    BRACKNELL = Location(
        id="58dde0de-7863-4ec4-8dbd-929fd223ccdf",
        name="Bracknell",
    )

    BRIGHTON_LONDON_ROAD = Location(
        id="486df9c7-3fdf-454e-812c-4ab609b53a2d",
        name="Brighton London Road",
    )

    BRIGHTON_MADEIRA_DRIVE = Location(
        id="f603f43f-f65c-42ad-bb0f-7c0ecac0eedc",
        name="Brighton Madeira Drive",
    )

    BRISTOL_AVONMEADS = Location(
        id="a4d845b0-bf3f-4e6b-82c2-bb80bef05994",
        name="Bristol Avonmeads",
    )

    BRISTOL_CITY_CENTRE = Location(
        id="16703291-b3b2-4ab5-9e32-c8057f89e7b5",
        name="Bristol City Centre",
    )

    BRISTOL_LONGWELL_GREEN = Location(
        id="5dbfa104-0360-42da-8c03-0792773c5437",
        name="Bristol Longwell Green",
    )

    BURNLEY = Location(
        id="d5d1ba31-a57f-4ce0-8859-99ba87c5fe8a",
        name="Burnley",
    )

    BURTON_UPON_TRENT = Location(
        id="dbfc8d2f-180d-4d57-ab8c-bd1554f14928",
        name="Burton upon Trent",
    )

    BURY_ST_EDMUNDS = Location(
        id="9e38e69c-24c7-401c-b761-c9bb2f4dac00",
        name="Bury St Edmunds",
    )

    CAMBRIDGE = Location(
        id="73f5344c-1cd1-41c2-b90a-f4f23e5b35e6",
        name="Cambridge",
    )

    CARDIFF_CITY_CENTRE = Location(
        id="2b06de6b-0090-4f11-8723-b8dd90b68b7e",
        name="Cardiff City Centre",
    )

    CARDIFF_NEWPORT_ROAD = Location(
        id="1901f9dc-ab4b-4499-aa32-8e72afc69543",
        name="Cardiff Newport Road",
    )

    CARLISLE = Location(
        id="ffe356e9-1d6e-40d7-bfd1-78fcd9f798b8",
        name="Carlisle",
    )

    CHELMSFORD = Location(
        id="d542da86-d999-448c-98d6-784e78e1b537",
        name="Chelmsford",
    )

    CHELTENHAM = Location(
        id="72ae0fbd-11b9-4d37-aa23-d3bc643f8931",
        name="Cheltenham",
    )

    CHESTER_CITY_CENTRE = Location(
        id="85c65060-ca53-4e57-9f07-8fb59491fc19",
        name="Chester City Centre",
    )

    CHESTERFIELD = Location(
        id="38fffc25-d268-418d-9a12-4c472966b6cc",
        name="Chesterfield",
    )

    CHICHESTER = Location(
        id="1aa6e9c8-0871-4bee-a7b1-a93ae2d29301",
        name="Chichester",
    )

    COLCHESTER = Location(
        id="57f72618-971f-4425-a434-3e8ee6bf34a2",
        name="Colchester",
    )

    COVENTRY = Location(
        id="8f339838-0af3-496e-8765-445cc32eb85f",
        name="Coventry",
    )

    CRAWLEY = Location(
        id="5637f713-3cf2-430b-a255-4262d87891df",
        name="Crawley",
    )

    DAGENHAM = Location(
        id="ec5933be-e969-4842-8ff0-6e8d4ee0b04a",
        name="Dagenham",
    )

    DARLINGTON = Location(
        id="7e6c135b-8b94-44ca-af19-180db09c13f9",
        name="Darlington",
    )

    DARTFORD = Location(
        id="1576d00c-9363-4c2a-ac7b-ace03d7a844d",
        name="Dartford",
    )

    DERBY = Location(
        id="47bb8464-7cbd-4903-9499-97b95267cea3",
        name="Derby",
    )

    DONCASTER = Location(
        id="6153ee19-55d8-40f8-95fe-10c48affdf31",
        name="Doncaster",
    )

    DORCHESTER = Location(
        id="154be905-8876-4de9-9062-d7102ba4b091",
        name="Dorchester",
    )

    DUNDEE = Location(
        id="5adb3221-8221-4af2-806e-3d0df0e1fb35",
        name="Dundee",
    )

    EASTBOURNE = Location(
        id="3cd22aea-f9f1-4ee1-bc3c-94ed346174cd",
        name="Eastbourne",
    )

    EDINBURGH_CAMERON_TOLL = Location(
        id="6c333b37-4177-4060-9afb-f9c78eba5947",
        name="Edinburgh Cameron Toll",
    )

    EDINBURGH_CITY = Location(
        id="84174cd1-19ac-4115-ad0f-d95820b964ce",
        name="Edinburgh City",
    )

    EDINBURGH_CORSTORPHINE = Location(
        id="e615e26b-bbc1-45c0-b758-fb6b85df9dda",
        name="Edinburgh Corstorphine",
    )

    EDINBURGH_MURRAYFIELD = Location(
        id="c9ddc56d-4f19-4e96-81c3-30db13f1a62c",
        name="Edinburgh Murrayfield",
    )

    EDINBURGH_STRAITON = Location(
        id="afc99ec7-0a4d-41b1-8fea-c59c2672853e",
        name="Edinburgh Straiton",
    )

    EXETER_MARSH_BARTON = Location(
        id="f52e29bb-88dd-4e99-97cd-6fd26860f792",
        name="Exeter Marsh Barton",
    )

    FAREHAM_LOCKS_HEATH = Location(
        id="61d90c39-1666-4dba-82f5-afa6ca8c8428",
        name="Fareham Locks Heath",
    )

    FARNBOROUGH = Location(
        id="042c2688-25ef-4e6c-bc71-0ad4fd46db54",
        name="Farnborough",
    )

    GLASGOW_ANNIESLAND = Location(
        id="363bf75c-98d0-4b8d-b12a-1a3d6717f718",
        name="Glasgow Anniesland",
    )

    GLASGOW_BOTHWELL_STREET = Location(
        id="641a6b11-f815-4829-bd26-be32bd54b7b5",
        name="Glasgow Bothwell Street",
    )

    GLASGOW_CITY = Location(
        id="44ec630d-eae3-4db1-9fec-9edead9a2145",
        name="Glasgow City",
    )

    GLASGOW_FORGE = Location(
        id="d838bd83-d494-4bd4-a40d-f10a0e184f34",
        name="Glasgow Forge",
    )

    GLASGOW_QUAY = Location(
        id="f0aa6b58-d0a6-4ddb-838d-f665d8863dc5",
        name="Glasgow Quay",
    )

    GLASGOW_SOUTH = Location(
        id="8779a1a5-27ac-4c34-ad87-69f4d166c6a2",
        name="Glasgow South",
    )

    GLASGOW_WEST_END = Location(
        id="2c4b55ef-b471-46dc-8515-9770c3bd348e",
        name="Glasgow West End",
    )

    GLENROTHES = Location(
        id="d6258ad0-aed1-4956-98a2-acdb95ca356d",
        name="Glenrothes",
    )

    GLOUCESTER = Location(
        id="d912d5e8-ecc9-45e3-b098-9ca58dd59935",
        name="Gloucester",
    )

    GREAT_YARMOUTH = Location(
        id="5a8f914f-912b-4e21-b8d8-6c32a4b42d35",
        name="Great Yarmouth",
    )

    GRIMSBY = Location(
        id="a9eee984-b5ed-4cec-8839-31cf1780befa",
        name="Grimsby",
    )

    GUILDFORD = Location(
        id="6823eae4-d508-4fb0-b890-e2aaef422702",
        name="Guildford",
    )

    HAMILTON = Location(
        id="a501b675-5a99-4564-9009-1b6bc4d3c3ee",
        name="Hamilton",
    )

    HANDFORTH_WILMSLOW = Location(
        id="c8c38f03-09cb-4230-a9c7-bfd38f08011a",
        name="Handforth Wilmslow",
    )

    HARTLEPOOL = Location(
        id="220a6453-2bdc-4f79-be37-5f90fd695b06",
        name="Hartlepool",
    )

    HASTINGS = Location(
        id="b2ac4f89-bc42-4e09-90f4-d23487bbc7e4",
        name="Hastings",
    )

    HEMEL_HEMPSTEAD = Location(
        id="04d081d1-8755-4640-a854-0e4082ea9203",
        name="Hemel Hempstead",
    )

    HIGH_WYCOMBE = Location(
        id="9d77f35e-f4ea-441d-a53e-1c035f88de3f",
        name="High Wycombe",
    )

    HINCKLEY = Location(
        id="f8a0badf-df56-4c7e-b8b1-184fcbff529d",
        name="Hinckley",
    )

    HORSHAM = Location(
        id="06a07d9a-bebd-480b-a408-2e18ba69a201",
        name="Horsham",
    )

    HOVE = Location(
        id="c48fb80f-83f1-4fd2-b23b-d56fc7ed48a8",
        name="Hove",
    )

    HUDDERSFIELD = Location(
        id="b7360068-ccff-478c-9914-95b14064fe14",
        name="Huddersfield",
    )

    HUNTINGDON = Location(
        id="9f230f3e-721d-4e97-b4f7-1c1e5a34dfd5",
        name="Huntingdon",
    )

    IPSWICH = Location(
        id="a965ac1b-3652-4475-a22a-c6fe760fbd4f",
        name="Ipswich",
    )

    IRVINE = Location(
        id="b72e4cf3-b501-4002-a370-8cdf03c1a99f",
        name="Irvine",
    )

    ISLE_OF_WIGHT = Location(
        id="ceb76b0d-589f-4b68-945f-e7d50fcb20de",
        name="Isle of Wight",
    )

    KIDDERMINSTER = Location(
        id="8decbb52-e3ef-4b38-a856-a86953f3ceb4",
        name="Kidderminster",
    )

    KILMARNOCK = Location(
        id="f4ce962d-e11c-494d-bdc0-9dd8eb576bad",
        name="Kilmarnock",
    )

    KINGS_LYNN = Location(
        id="9cad67f1-d222-4568-9053-a5cba2ad78df",
        name="Kings Lynn",
    )

    LEEDS_HEADINGLEY = Location(
        id="b08f7f9e-10f6-4c5b-8af6-5dcb50feb227",
        name="Leeds Headingley",
    )

    LEEDS_HEADROW = Location(
        id="4ae1175a-e068-4878-b200-8d2621efdf42",
        name="Leeds Headrow",
    )

    LEEDS_MEANWOOD = Location(
        id="1a569a6e-d1bd-4b85-aacb-ee93d96c26dd",
        name="Leeds Meanwood",
    )

    LEEDS_YORK_ROAD = Location(
        id="774da2fc-47c8-4ee3-8706-04f1209f4fed",
        name="Leeds York Road",
    )

    LEICESTER_AYLESTONE_ROAD = Location(
        id="0e1de807-4988-4940-ba30-4d04dc1a6209",
        name="Leicester Aylestone Road",
    )

    LEICESTER_HIGHCROSS = Location(
        id="96771c3f-f295-4061-9511-0b03d7c1c301",
        name="Leicester Highcross",
    )

    LEYLAND = Location(
        id="735c3fd5-29d6-4599-aa32-39298f0c31c3",
        name="Leyland",
    )

    LIVERPOOL_CENTRAL = Location(
        id="3a04c1b9-fbc7-4ff9-b040-ac72ee857989",
        name="Liverpool Central",
    )

    LIVERPOOL_GREAT_HOMER_STREET = Location(
        id="ef627113-b609-4ad6-a1e8-346fc4a3de78",
        name="Liverpool Great Homer Street",
    )

    LIVERPOOL_ONE = Location(
        id="90922d7a-e1b0-4854-ae55-5af591c1195c",
        name="Liverpool One",
    )

    LONDON_ACTON = Location(
        id="1bdeaf9b-37b1-42ee-9a6c-b8d82b86b7ad",
        name="London Acton",
    )

    LONDON_ALPERTON = Location(
        id="077c1e98-eb8c-4f54-a52e-dce702ad196e",
        name="London Alperton",
    )

    LONDON_ANGEL = Location(
        id="45110b28-29b3-4678-b581-824dcea0b85f",
        name="London Angel",
    )

    LONDON_BARKING = Location(
        id="052a490a-7602-4ba6-96e1-7bdf610c4a51",
        name="London Barking",
    )

    LONDON_BATTERSEA = Location(
        id="22452ecd-d8ca-4859-b676-f400b41b482b",
        name="London Battersea",
    )

    LONDON_BLOOMSBURY = Location(
        id="ff30f44f-cd31-4d61-8dcc-1af301c3d93c",
        name="London Bloomsbury",
    )

    LONDON_CALEDONIAN_ROAD = Location(
        id="d4918f5e-9765-4c9d-9767-092de42ba0c5",
        name="London Caledonian Road",
    )

    LONDON_CANNING_TOWN = Location(
        id="748f6ac2-0a8e-4ad0-8c0b-8de5e6cb14ab",
        name="London Canning Town",
    )

    LONDON_CATFORD = Location(
        id="58cf98f7-68e3-4371-9e22-3ca14842b5e9",
        name="London Catford",
    )

    LONDON_CHADWELL_HEATH = Location(
        id="7487644d-eba2-4d29-804a-fa8f2a098b5f",
        name="London Chadwell Heath",
    )

    LONDON_CHARING_CROSS = Location(
        id="a730cd44-38c7-48c9-92b6-b5641dbc980b",
        name="London Charing Cross",
    )

    LONDON_COLINDALE = Location(
        id="597e4b50-73c6-43cd-b700-60efbcb4ef00",
        name="London Colindale",
    )

    LONDON_COLLIERS_WOOD = Location(
        id="3e98ff30-ed54-4217-bcad-df5000c3eacd",
        name="London Colliers Wood",
    )

    LONDON_CROYDON_PURLEY_WAY = Location(
        id="dd86d891-69b9-404d-95de-469cb3c1ad26",
        name="London Croydon Purley Way",
    )

    LONDON_EALING = Location(
        id="3b0d6bbe-7720-4f37-8dc3-6824f507ceb9",
        name="London Ealing",
    )

    LONDON_EAST_CROYDON = Location(
        id="941dbda3-e751-4677-83fd-c3ff4d175e0b",
        name="London East Croydon",
    )

    LONDON_EAST_HAM_HIGH_STREET = Location(
        id="c3415116-ac46-43c9-b79b-fe7db5ae07b1",
        name="London East Ham High Street",
    )

    LONDON_EDMONTON_GREEN = Location(
        id="17aad54f-3411-4b1c-ae97-c6b10eab3e4d",
        name="London Edmonton Green",
    )

    LONDON_EUSTON_ROAD = Location(
        id="944f52a4-d661-4e75-9bda-328830a5c21c",
        name="London Euston Road",
    )

    LONDON_FELTHAM = Location(
        id="444237d6-7d56-4191-9ebb-975615fa1fca",
        name="London Feltham",
    )

    LONDON_FULHAM = Location(
        id="088f5cd7-ebf2-4dd2-8555-0a218229115e",
        name="London Fulham",
    )

    LONDON_GREENWICH = Location(
        id="2473d9c3-5c78-44c0-b05a-3d1a4310b709",
        name="London Greenwich",
    )

    LONDON_HARRINGAY = Location(
        id="05e73825-eeab-4d87-a632-c194ff9b4c2a",
        name="London Harringay",
    )

    LONDON_HARROW_ON_THE_HILL = Location(
        id="93cee414-d4d4-44a8-a012-79bac8bcdc31",
        name="London Harrow on the Hill",
    )

    LONDON_HOLBORN_CIRCUS = Location(
        id="a43a1a3e-e920-46ed-a452-86de309ebd16",
        name="London Holborn Circus",
    )

    LONDON_HOUNSLOW = Location(
        id="17581ba4-e6b6-4fd1-9a6f-55ecd0bf960a",
        name="London Hounslow",
    )

    LONDON_ILFORD_PIONEER_POINT = Location(
        id="d26d13ca-43c6-49d6-97a1-a64a2b369e90",
        name="London Ilford Pioneer Point",
    )

    LONDON_ILFORD_ROMFORD_ROAD = Location(
        id="e77257e2-5b56-40ef-8989-761f98d854c5",
        name="London Ilford Romford Road",
    )

    LONDON_KINGSBURY = Location(
        id="5f088d5d-c5ed-4ac8-b35e-2f93ff9cd6f5",
        name="London Kingsbury",
    )

    LONDON_KINGSTON = Location(
        id="a6ca74a3-13e3-42c5-9c99-45b416d93c8e",
        name="London Kingston",
    )

    LONDON_LEWISHAM = Location(
        id="6f056c6e-9194-43fd-80d7-e8c0053a2aee",
        name="London Lewisham",
    )

    LONDON_MANOR_HOUSE = Location(
        id="28bd11f5-6179-4c35-a487-dc699b222a80",
        name="London Manor House",
    )

    LONDON_MONUMENT = Location(
        id="7a8b74fc-3f9b-480b-b20c-e27c42a34f1b",
        name="London Monument",
    )

    LONDON_NORBURY = Location(
        id="b8ce030d-8c36-4388-b4f5-911810d1329e",
        name="London Norbury",
    )

    LONDON_NORTH_HARROW = Location(
        id="97738448-4071-4b32-86a6-c0fe367b7022",
        name="London North Harrow",
    )

    LONDON_OXFORD_STREET = Location(
        id="25b587ab-3541-4334-9525-caa8e7b7f878",
        name="London Oxford Street",
    )

    LONDON_PADDINGTON = Location(
        id="bbf20161-169c-4846-9c2c-2cd70fd13a2f",
        name="London Paddington",
    )

    LONDON_PECKHAM_RYE = Location(
        id="74b46743-fb5d-4612-9ad9-f4b7e8feb1e5",
        name="London Peckham Rye",
    )

    LONDON_SOUTH_RUISLIP = Location(
        id="2cdadf86-5afb-4f41-aa22-fdc1fb1500ec",
        name="London South Ruislip",
    )

    LONDON_SOUTHALL = Location(
        id="be713a87-6992-4885-a041-5e0dc2b16c26",
        name="London Southall",
    )

    LONDON_SOUTHFIELDS = Location(
        id="0d17c5af-ec5a-4b4a-a479-2c519158a6ef",
        name="London Southfields",
    )

    LONDON_STAPLES_CORNER = Location(
        id="d2b21280-0598-4678-b801-3ff2d009340b",
        name="London Staples Corner",
    )

    LONDON_STEPNEY_GREEN = Location(
        id="ced1be11-df42-43da-b790-29cffe735dac",
        name="London Stepney Green",
    )

    LONDON_STOCKWELL = Location(
        id="f98d7176-fc95-4c2f-9dfe-9348763d860d",
        name="London Stockwell",
    )

    LONDON_STREATHAM = Location(
        id="d39aca8e-b454-4b88-86cb-03803b20cf57",
        name="London Streatham",
    )

    LONDON_SUNBURY = Location(
        id="1e38ce55-8a05-4822-8671-57f29486f5d9",
        name="London Sunbury",
    )

    LONDON_SUTTON = Location(
        id="ad5de35b-0b26-4d21-b804-b069f8ef60bf",
        name="London Sutton",
    )

    LONDON_SYDENHAM = Location(
        id="09b69bff-4249-47cc-bacb-32ccbc842f85",
        name="London Sydenham",
    )

    LONDON_TOOTING = Location(
        id="6082ef3f-d993-41eb-bc63-b88d5c770ee3",
        name="London Tooting",
    )

    LONDON_TOTTENHAM_HALE = Location(
        id="3a9d6c11-b640-4452-9c0e-a34e0723e247",
        name="London Tottenham Hale",
    )

    LONDON_TOTTENHAM_HIGH_ROAD = Location(
        id="00c11586-0b1e-4daa-8ccb-fadacb40fa41",
        name="London Tottenham High Road",
    )

    LONDON_TOTTENHAM_WHITE_HART_LANE = Location(
        id="9b41838b-cf0f-432d-b8cc-d11bd797b6c2",
        name="London Tottenham White Hart Lane",
    )

    LONDON_VAUXHALL = Location(
        id="d7511589-7fdc-40f1-a966-c89b8171ee95",
        name="London Vauxhall",
    )

    LONDON_WALTHAMSTOW = Location(
        id="3e78d629-115d-40fe-807c-b8185539f7ab",
        name="London Walthamstow",
    )

    LONDON_WALWORTH_ROAD = Location(
        id="6fa61e87-b1f2-47c1-8191-a403e281047a",
        name="London Walworth Road",
    )

    LONDON_WANDSWORTH = Location(
        id="43592dc0-b328-4620-b09e-bb4f1c57d9e6",
        name="London Wandsworth",
    )

    LONDON_WATERLOO = Location(
        id="c6b1c66e-7df5-484f-aa62-50da1d968d25",
        name="London Waterloo",
    )

    LONDON_WEALDSTONE = Location(
        id="26e5f1bd-f841-4bb1-8537-27cd703bd62a",
        name="London Wealdstone",
    )

    LONDON_WEMBLEY_CENTRAL = Location(
        id="18147c4d-3473-4848-b1aa-05404ce51c9b",
        name="London Wembley Central",
    )

    LONDON_WEMBLEY_PARK = Location(
        id="256fedcd-6d01-4498-8c7f-048ae5702ad8",
        name="London Wembley Park",
    )

    LONDON_WEST_CROYDON = Location(
        id="198c6ba2-149c-4279-9cb2-3bd58077ae0f",
        name="London West Croydon",
    )

    LONDON_WEST_HAMPSTEAD = Location(
        id="6c3183f9-7e9d-4abf-851b-eb940e5ee965",
        name="London West Hampstead",
    )

    LONDON_WOOD_GREEN_LORDSHIP_LANE = Location(
        id="0966c8af-94d1-4ad6-8e77-40b8272faef5",
        name="London Wood Green Lordship Lane",
    )

    LONDON_WOOD_GREEN_THE_MALL = Location(
        id="c67b143d-9017-419f-9e89-fa3c500b9169",
        name="London Wood Green The Mall",
    )

    LOWESTOFT = Location(
        id="c32261a7-f8b3-4705-bb8e-b1e126ab25ad",
        name="Lowestoft",
    )

    LUTON = Location(
        id="d37536f0-ee7f-406e-8695-fb170d3e8eac",
        name="Luton",
    )

    MANCHESTER_ASHTON_OLD_ROAD = Location(
        id="711e7e1c-bc5d-44a7-981f-2912b2ebe7e8",
        name="Manchester Ashton Old Road",
    )

    MANCHESTER_DEANSGATE = Location(
        id="6e6f686f-8443-4ea5-8836-59714085aa5d",
        name="Manchester Deansgate",
    )

    MANCHESTER_FALLOWFIELD = Location(
        id="db35298c-60c0-4054-9ba2-bb97b01ed938",
        name="Manchester Fallowfield",
    )

    MANCHESTER_OLD_TRAFFORD = Location(
        id="212fb61a-2945-488d-8385-6e03bbc257db",
        name="Manchester Old Trafford",
    )

    MANCHESTER_PORTLAND_STREET = Location(
        id="bf482489-461c-4ca3-b435-fa265a7826bf",
        name="Manchester Portland Street",
    )

    MANCHESTER_WHITEFIELD = Location(
        id="889c78eb-d9bb-4055-aeb3-43f173ff1be9",
        name="Manchester Whitefield",
    )

    MIDDLESBROUGH = Location(
        id="3ef91528-3376-4690-8454-65a50efe171c",
        name="Middlesbrough",
    )

    MIDSOMER_NORTON = Location(
        id="e013055a-4897-433f-a854-375dabf2c832",
        name="Midsomer Norton",
    )

    MILTON_KEYNES = Location(
        id="f01bd60a-39b7-452c-966b-94322f9c4ffb",
        name="Milton Keynes",
    )

    NEWARK = Location(
        id="c1530df9-7be4-40b1-8a73-e07aefa87164",
        name="Newark",
    )

    NEWCASTLE_CITY = Location(
        id="e5bafaa8-583d-4d19-9550-92848e0d173d",
        name="Newcastle City",
    )

    NEWCASTLE_EAST = Location(
        id="b2b241ff-e070-4365-85ba-c80f78f0ee22",
        name="Newcastle East",
    )

    NEWCASTLE_GOSFORTH = Location(
        id="4f0c15a1-1647-40de-9c2b-0ae5827c8634",
        name="Newcastle Gosforth",
    )

    NEWTON_ABBOT = Location(
        id="5b400f43-b160-403a-a35b-86ded56e5d5d",
        name="Newton Abbot",
    )

    NORTHAMPTON = Location(
        id="9da979ab-fa61-4aab-8872-b306d4c5a8cc",
        name="Northampton",
    )

    NORTHAMPTON_CENTRAL = Location(
        id="1b0d972c-c1a1-4ee7-9f92-40d0f1a8f81f",
        name="Northampton Central",
    )

    NORWICH_CITY = Location(
        id="74918a11-f754-43ac-a529-da7274cd98c0",
        name="Norwich City",
    )

    NORWICH_HALL_ROAD = Location(
        id="9917ddc9-62ec-4f69-9538-a05da83116b6",
        name="Norwich Hall Road",
    )

    NOTTINGHAM_CHILWELL = Location(
        id="cf559520-9e36-4d88-a1f8-951d2c227961",
        name="Nottingham Chilwell",
    )

    NOTTINGHAM_CITY = Location(
        id="f124bb76-f73c-43e8-a165-098846aa8dc6",
        name="Nottingham City",
    )

    NOTTINGHAM_RADFORD = Location(
        id="a107613f-4c66-46f6-8ec2-f3159651612f",
        name="Nottingham Radford",
    )

    NOTTINGHAM_SHERWOOD = Location(
        id="1d51de30-cfdb-41c5-95e3-c34c22c303a1",
        name="Nottingham Sherwood",
    )

    OADBY = Location(
        id="0ede64e3-c8f9-489d-93e4-b89754c394a1",
        name="Oadby",
    )

    OLDHAM = Location(
        id="dde3b0b5-a830-49bd-9f1f-0439316e4100",
        name="Oldham",
    )

    OXFORD_ABINGDON = Location(
        id="59c6b1ab-8f65-4735-a3c9-50d22f7e50df",
        name="Oxford Abingdon",
    )

    OXFORD_HEADINGTON = Location(
        id="c2bb4c20-0f42-4048-943e-8af391e68dbb",
        name="Oxford Headington",
    )

    PAIGNTON = Location(
        id="36824bdb-4051-4d20-afda-6861ac2f3c01",
        name="Paignton",
    )

    PERTH = Location(
        id="64ac7f24-041d-42ed-a143-eb00248f90e8",
        name="Perth",
    )

    PETERBOROUGH = Location(
        id="4c7940a9-e30e-4e73-b1b9-0e30bca28676",
        name="Peterborough",
    )

    PLYMOUTH = Location(
        id="1473adb6-d3fa-4682-b14b-7bc6d59dff7b",
        name="Plymouth",
    )

    PLYMOUTH_LAIRA_BRIDGE = Location(
        id="3fbf9564-365a-4026-9895-359dac23a516",
        name="Plymouth Laira Bridge",
    )

    POOLE = Location(
        id="4b9dfab6-87e0-4b6c-b718-1a8d1b9835a9",
        name="Poole",
    )

    PORTSMOUTH_FRATTON = Location(
        id="9edb5be3-8449-48b2-ac93-e49833091ea7",
        name="Portsmouth Fratton",
    )

    READING_CENTRAL = Location(
        id="a0635a53-4320-4e27-b63e-9fb77a3eeb7b",
        name="Reading Central",
    )

    READING_WEST = Location(
        id="bbedefae-4961-4581-929d-c98839d494ad",
        name="Reading West",
    )

    REDHILL = Location(
        id="86446945-03b1-4f18-b9ea-ef33adc5da28",
        name="Redhill",
    )

    ROMFORD = Location(
        id="ac6ab55d-b0ed-47c6-ab53-b7749867a839",
        name="Romford",
    )

    ROTHERHAM = Location(
        id="a43a1ac0-cebf-4a82-8a2f-ab78ca1433f2",
        name="Rotherham",
    )

    SCUNTHORPE_LAKESIDE = Location(
        id="bc93c61e-015d-40c3-80f9-786c80dcb0bf",
        name="Scunthorpe Lakeside",
    )

    SHEFFIELD_KELHAM_ISLAND = Location(
        id="a7cb814d-7229-4487-86fc-cabee3951220",
        name="Sheffield Kelham Island",
    )

    SHEFFIELD_THE_MOOR = Location(
        id="5c1f8013-1d1a-40ff-8049-f9d3c5d4d209",
        name="Sheffield The Moor",
    )

    SHIRLEY_SOLIHULL = Location(
        id="52eca135-f7ab-4e2a-a553-ae56348edfe1",
        name="Shirley Solihull",
    )

    SLOUGH = Location(
        id="b890c1ab-40f1-4bf5-9458-509e9fd08d76",
        name="Slough",
    )

    SOUTH_SHIELDS = Location(
        id="2210d354-e7cd-45f2-bc6d-fdfdf2ef4b5d",
        name="South Shields",
    )

    SOUTHAMPTON_CENTRAL = Location(
        id="17df3def-4ef0-4536-9b46-b7cb977d1da0",
        name="Southampton Central",
    )

    SOUTHAMPTON_EAST = Location(
        id="57fd25e9-7aca-4652-b4ac-6699fcd2bd53",
        name="Southampton East",
    )

    SOUTHAMPTON_PORTSWOOD = Location(
        id="8e88da91-a715-4124-9a27-c1e656b9249f",
        name="Southampton Portswood",
    )

    SOUTHAMPTON_SHIRLEY = Location(
        id="98927adb-e0b4-4957-b066-cc087dae2246",
        name="Southampton Shirley",
    )

    SOUTHEND = Location(
        id="53eb0dd5-cc17-4be8-b999-a67b03ff959b",
        name="Southend",
    )

    STAFFORD = Location(
        id="5cf8507c-94fb-42b5-8e93-9ae13ccda6b8",
        name="Stafford",
    )

    STOCKPORT = Location(
        id="bc9204a7-7ce6-4e78-a782-51adcb98297c",
        name="Stockport",
    )

    STOURBRIDGE = Location(
        id="2fa47cb4-8977-48d2-8fc5-03d3fde4883c",
        name="Stourbridge",
    )

    STROOD = Location(
        id="a0e4d62e-e37d-46cb-b9b0-de58b458bebc",
        name="Strood",
    )

    SUNDERLAND_SOUTH = Location(
        id="42037007-ba30-4288-9c3a-c072d1294910",
        name="Sunderland South",
    )

    SUTTON_COLDFIELD = Location(
        id="89ec1654-321f-409e-9c6a-7a3edd3e4f8e",
        name="Sutton Coldfield",
    )

    SWANSEA = Location(
        id="708ae094-286f-4524-8fa8-b1ff65dbd247",
        name="Swansea",
    )

    SWINDON = Location(
        id="fb7371be-0c40-4f5b-85ef-11f3ace5f647",
        name="Swindon",
    )

    TAMWORTH = Location(
        id="e7a999ba-7b43-439e-ba26-c97985b72871",
        name="Tamworth",
    )

    TELFORD = Location(
        id="7963251a-1688-4f4a-bd16-3d102e3c6305",
        name="Telford",
    )

    THANET = Location(
        id="9cbab9b4-1e9b-4236-b3b5-c463167d43fc",
        name="Thanet",
    )

    UXBRIDGE = Location(
        id="6f699bf8-28a2-4b8a-ae3c-5540047c5fb9",
        name="Uxbridge",
    )

    WAKEFIELD = Location(
        id="3b83a143-ff86-42cd-9887-c4fa4c5bc278",
        name="Wakefield",
    )

    WATFORD = Location(
        id="20495b17-55e5-46f6-b328-dfbd7c55175a",
        name="Watford",
    )

    WIMBLEDON = Location(
        id="5f8d275e-6855-4eac-810a-36ca646a7159",
        name="Wimbledon",
    )

    WOKING = Location(
        id="6be2b33e-149c-4b8f-831b-179cc39b467a",
        name="Woking",
    )

    WOLVERHAMPTON = Location(
        id="1a23bf9e-c215-4ca6-976a-a1cea577f8f2",
        name="Wolverhampton",
    )

    WORTHING = Location(
        id="95e978f4-f16d-494b-a030-fa608c5942e4",
        name="Worthing",
    )

    YORK_FOSS_ISLAND = Location(
        id="e6fde50a-91df-4a5b-b936-4118d2432cb8",
        name="York Foss Island",
    )


def list_locations() -> Iterable[Location]:
    for value in vars(Locations).values():
        if isinstance(value, Location):
            yield value


def resolve_location(location: Location | str) -> str:
    if isinstance(location, Location):
        return location.id
    if isinstance(location, str):
        UUID(location)
        return location
