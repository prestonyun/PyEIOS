#    Copyright 2020 by Brett J. Moan
#
#    This file is part of pyautoeios.
#
#    pyautoeios is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    pyautoeios is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with pyautoeios.  If not, see <https://www.gnu.org/licenses/>.
import collections

THook = collections.namedtuple("THook", "cls field desc multiplier")


def hook(c: str, f: str, d: str, m: int):
    return THook(c.encode("utf8"), f.encode("utf8"), d.encode("utf8"), m)


NODE_UID = hook("sj", "hq", "J", 1)
NODE_PREV = hook("sj", "hw", "Lsj;", 1)
NODE_NEXT = hook("sj", "hy", "Lsj;", 1)
NODEDEQUE_HEAD = hook("ow", "au", "Lsj;", 1)
NODEDEQUE_CURRENT = hook("ow", "ae", "Lsj;", 1)
CACHEABLE_NEXT = hook("sq", "er", "Lsq;", 1)
CACHEABLE_PREV = hook("sq", "ea", "Lsq;", 1)
LINKEDLIST_HEAD = hook("oc", "au", "Lsj;", 1)
LINKEDLIST_CURRENT = hook("oc", "ae", "Lsj;", 1)
HASHTABLE_HEAD = hook("so", "ao", "Lsj;", 1)
HASHTABLE_TAIL = hook("so", "at", "Lsj;", 1)
HASHTABLE_BUCKETS = hook("so", "ae", "[Lsj;", 1)
HASHTABLE_INDEX = hook("so", "ac", "I", 1)
HASHTABLE_SIZE = hook("so", "au", "I", 1)
ITERABLEHASHTABLE_HEAD = hook("sf", "ao", "Lsj;", 1)
ITERABLEHASHTABLE_TAIL = hook("sf", "at", "Lsj;", 1)
ITERABLEHASHTABLE_BUCKETS = hook("sf", "ae", "[Lsj;", 1)
ITERABLEHASHTABLE_INDEX = hook("sf", "ac", "I", 1)
ITERABLEHASHTABLE_SIZE = hook("sf", "au", "I", 1)
QUEUE_HEAD = hook("ou", "ae", "Lsq;", 1)
CACHE_HASHTABLE = hook("le", "at", "Lsf;", 1)
CACHE_QUEUE = hook("le", "ac", "Lou;", 1)
CACHE_REMAINING = hook("le", "ao", "I", 1)
CACHE_CAPACITY = hook("le", "ae", "I", 1)
CLASSDATA_BYTES = hook("ba", "ap", "[[[B", 1)
CLASSDATA_METHODS = hook("ba", "az", "[Ljava/lang/reflect/Method;", 1)
CLASSDATA_FIELDS = hook("ba", "ac", "[Ljava/lang/reflect/Field;", 1)
RASTERISER_PIXELS = hook("ut", "av", "[I", 1)
RASTERISER_WIDTH = hook("ut", "aw", "I", 1)
RASTERISER_HEIGHT = hook("ut", "ak", "I", 1)
RASTERISER3D_SHADOWDECAY = hook("N/A", "N/A", "N/A", 1)
RASTERISER3D_SINETABLE = hook("ix", "at", "[I", 1)
RASTERISER3D_COSINETABLE = hook("ix", "ac", "[I", 1)
TYPEFACE_CHARACTERPIXELS = hook("pk", "ae", "[[B", 1)
INDEXEDRGB_PIXELS = hook("uk", "au", "[B", 1)
INDEXEDRGB_PALETTE = hook("uk", "ae", "[I", 1)
INDEXEDRGB_WIDTH = hook("uk", "az", "I", 1)
INDEXEDRGB_HEIGHT = hook("uk", "ap", "I", 1)
IMAGERGB_PIXELS = hook("ui", "au", "[I", 1)
IMAGERGB_WIDTH = hook("ui", "ae", "I", 1)
IMAGERGB_HEIGHT = hook("ui", "ao", "I", 1)
IMAGERGB_MAXWIDTH = hook("ui", "ai", "I", 1)
IMAGERGB_MAXHEIGHT = hook("ui", "az", "I", 1)
BUFFER_PAYLOAD = hook("tm", "ap", "[B", 1)
BUFFER_CRC = hook("tm", "af", "[I", 1)
BUFFEREDCONNECTION_INPUTSTREAM = hook("N/A", "N/A", "N/A", 1)
BUFFEREDCONNECTION_OUTPUTSTREAM = hook("N/A", "N/A", "N/A", 1)
BUFFEREDCONNECTION_SOCKET = hook("N/A", "N/A", "N/A", 1)
BUFFEREDCONNECTION_PAYLOAD = hook("N/A", "N/A", "N/A", 1)
BUFFEREDCONNECTION_ISCLOSED = hook("N/A", "N/A", "N/A", 1)
COLLISIONMAP_WIDTH = hook("is", "bf", "I", -1421950985)
COLLISIONMAP_HEIGHT = hook("is", "bq", "I", 1927939041)
COLLISIONMAP_ADJACENCY = hook("is", "ba", "[[I", 1)
NAMEINFO_NAME = hook("uc", "au", "Ljava/lang/String;", 1)
NAMEINFO_DECODEDNAME = hook("uc", "ae", "Ljava/lang/String;", 1)
RENDERABLE_MODELHEIGHT = hook("ik", "eq", "I", 1008243717)
REGION_SCENETILES = hook("iv", "ai", "[[[Lii;", 1)
REGION_INTERACTABLEOBJECTS = hook("iv", "bt", "[Ljy;", 1)
ANIMABLENODE_ID = hook("dj", "au", "I", -1501685719)
ANIMABLENODE_ANIMATIONSEQUENCE = hook("dj", "az", "Lib;", 1)
ANIMABLENODE_FLAGS = hook("dj", "ae", "I", -75702939)
ANIMABLENODE_ORIENTATION = hook("dj", "ao", "I", -231241725)
ANIMABLENODE_PLANE = hook("dj", "at", "I", 215686393)
ANIMABLENODE_X = hook("dj", "ac", "I", 795738445)
ANIMABLENODE_Y = hook("dj", "ai", "I", -1260218321)
ANIMABLENODE_ANIMATIONFRAME = hook("dj", "ap", "I", 1287923743)
BOUNDARYOBJECT_ID = hook("jo", "ap", "J", -4244623663237435829)
BOUNDARYOBJECT_FLAGS = hook("jo", "aa", "I", 1002689579)
BOUNDARYOBJECT_PLANE = hook("jo", "au", "I", 1162218027)
BOUNDARYOBJECT_HEIGHT = hook("jo", "ac", "I", 1499438365)
BOUNDARYOBJECT_LOCALX = hook("jo", "ae", "I", 1928295169)
BOUNDARYOBJECT_LOCALY = hook("jo", "ao", "I", 2005175761)
BOUNDARYOBJECT_ORIENTATION = hook("jo", "at", "I", -1628547661)
BOUNDARYOBJECT_RENDERABLE = hook("jo", "ai", "Lik;", 1)
BOUNDARYOBJECT_RENDERABLE2 = hook("jo", "az", "Lik;", 1)
WALLDECORATION_ID = hook("jw", "af", "J", -5570150087619181313)
WALLDECORATION_FLAGS = hook("jw", "ad", "I", 1405593685)
WALLDECORATION_PLANE = hook("jw", "au", "I", -1365937923)
WALLDECORATION_HEIGHT = hook("jw", "ac", "I", 489110633)
WALLDECORATION_LOCALX = hook("jw", "ae", "I", 787946685)
WALLDECORATION_LOCALY = hook("jw", "ao", "I", -218934925)
WALLDECORATION_RELATIVEX = hook("jw", "ai", "I", 1102500453)
WALLDECORATION_RELATIVEY = hook("jw", "az", "I", 1708077931)
WALLDECORATION_ORIENTATION = hook("jw", "at", "I", 52639641)
WALLDECORATION_RENDERABLE = hook("jw", "ap", "Lik;", 1)
WALLDECORATION_RENDERABLE2 = hook("jw", "aa", "Lik;", 1)
FLOORDECORATION_ID = hook("iy", "ac", "J", -7416437096913740991)
FLOORDECORATION_FLAGS = hook("iy", "ai", "I", 416833439)
FLOORDECORATION_LOCALX = hook("iy", "ae", "I", -562400569)
FLOORDECORATION_LOCALY = hook("iy", "ao", "I", 170483739)
FLOORDECORATION_PLANE = hook("iy", "au", "I", -2013789607)
FLOORDECORATION_RENDERABLE = hook("iy", "at", "Lik;", 1)
GAMEOBJECT_RENDERABLE = hook("jy", "ac", "Lik;", 1)
GAMEOBJECT_ID = hook("jy", "al", "J", -613017502485947103)
GAMEOBJECT_FLAGS = hook("jy", "an", "I", -1630640933)
GAMEOBJECT_ORIENTATION = hook("jy", "ai", "I", 1562518895)
GAMEOBJECT_PLANE = hook("jy", "au", "I", 381693817)
GAMEOBJECT_HEIGHT = hook("jy", "ae", "I", 1663864411)
GAMEOBJECT_LOCALX = hook("jy", "ao", "I", -878868163)
GAMEOBJECT_LOCALY = hook("jy", "at", "I", 770343019)
GAMEOBJECT_WORLDX = hook("jy", "az", "I", 274645333)
GAMEOBJECT_WORLDY = hook("jy", "aa", "I", 1748940281)
GAMEOBJECT_OFFSETX = hook("jy", "ap", "I", 80120955)
GAMEOBJECT_OFFSETY = hook("jy", "af", "I", 1302717711)
GRAPHICSOBJECT_ID = hook("cg", "au", "I", 539793439)
GRAPHICSOBJECT_LOCALX = hook("cg", "at", "I", 540026663)
GRAPHICSOBJECT_LOCALY = hook("cg", "ac", "I", -37149761)
GRAPHICSOBJECT_HEIGHT = hook("cg", "ai", "I", 284515791)
GRAPHICSOBJECT_PLANE = hook("cg", "ao", "I", -49690437)
GRAPHICSOBJECT_SEQUENCEDEFINITION = hook("cg", "az", "Lib;", 1)
GRAPHICSOBJECT_FRAME = hook("cg", "ap", "I", -956501499)
GRAPHICSOBJECT_FRAMECYCLE = hook("cg", "aa", "I", -1971256985)
GRAPHICSOBJECT_STARTCYCLE = hook("cg", "ae", "I", 794022017)
GRAPHICSOBJECT_ISFINISHED = hook("cg", "af", "Z", 1)
SCENETILE_BOUNDARYOBJECT = hook("ii", "az", "Ljo;", 1)
SCENETILE_SCENETILEOBJECT = hook("ii", "aj", "Lii;", 1)
SCENETILE_GAMEOBJECTS = hook("ii", "aq", "[Ljy;", 1)
SCENETILE_WALLDECORATION = hook("ii", "ap", "Ljw;", 1)
SCENETILE_GROUNDDECORATION = hook("ii", "aa", "Liy;", 1)
SCENETILE_SCENEX = hook("ii", "ae", "I", 1079694399)
SCENETILE_SCENEY = hook("ii", "ao", "I", -1746194663)
SCENETILE_PLANE = hook("ii", "at", "I", -1776469753)
GRANDEXCHANGE_STATUS = hook("oh", "au", "B", 1)
GRANDEXCHANGE_ITEMID = hook("oh", "ae", "I", -1950661591)
GRANDEXCHANGE_PRICE = hook("oh", "ao", "I", -1417966657)
GRANDEXCHANGE_QUANTITY = hook("oh", "at", "I", 602808251)
GRANDEXCHANGE_TRANSFERRED = hook("oh", "ac", "I", -662672265)
GRANDEXCHANGE_SPENT = hook("oh", "ai", "I", -1815027607)
GRANDEXCHANGE_QUERYIDS = hook("N/A", "N/A", "N/A", 1)
MODEL_INDICESX = hook("jr", "al", "[I", 1)
MODEL_INDICESY = hook("jr", "an", "[I", 1)
MODEL_INDICESZ = hook("jr", "ar", "[I", 1)
MODEL_INDICESLENGTH = hook("jr", "aq", "I", 1)
MODEL_VERTICESX = hook("jr", "aa", "[I", 1)
MODEL_VERTICESY = hook("jr", "af", "[I", 1)
MODEL_VERTICESZ = hook("jr", "ad", "[I", 1)
MODEL_VERTICESLENGTH = hook("jr", "ap", "I", 1)
MODEL_TEXINDICESX = hook("jr", "ab", "[I", 1)
MODEL_TEXINDICESY = hook("jr", "ag", "[I", 1)
MODEL_TEXINDICESZ = hook("jr", "am", "[I", 1)
MODEL_TEXVERTICESX = hook("jr", "aw", "[I", 1)
MODEL_TEXVERTICESY = hook("jr", "ak", "[I", 1)
MODEL_TEXVERTICESZ = hook("jr", "bh", "[I", 1)
MODEL_TEXVERTICESLENGTH = hook("jr", "av", "I", 1)
MODEL_SKINS = hook("jr", "bj", "[[I", 1)
MODEL_FACECOLORS3 = hook("jr", "am", "[I", 1)
MODEL_SHADOWINTENSITY = hook("jr", "bk", "[[I", 1)
MODEL_FITSSINGLETILE = hook("jr", "bd", "Z", 1)
ANIMATIONSEQUENCE_FRAMES = hook("ib", "ar", "[I", 1)
ANIMATIONSEQUENCE_SEQUENCECACHE = hook("ib", "ap", "Lle;", 1)
ANIMATIONSEQUENCE_FRAMECACHE = hook("ib", "aa", "Lle;", 1)
ANIMATIONFRAMES_FRAMES = hook("jt", "au", "[Lia;", 1)
ANIMATIONSKELETON_ID = hook("iu", "ai", "I", -1820285713)
ANIMATIONSKELETON_TRANSFORMATIONCOUNT = hook("iu", "az", "I", -1247800495)
ANIMATIONSKELETON_TRANSFORMATIONTYPES = hook("iu", "ap", "[I", 1)
ANIMATIONSKELETON_TRANSFORMATIONS = hook("iu", "aa", "[[I", 1)
ANIMATION_FRAMECOUNT = hook("ia", "ai", "I", 1)
ANIMATION_TRANSFORMX = hook("ia", "ap", "[I", 1)
ANIMATION_TRANSFORMY = hook("ia", "aa", "[I", 1)
ANIMATION_TRANSFORMZ = hook("ia", "af", "[I", 1)
ANIMATION_FRAMES = hook("ia", "az", "[I", 1)
ANIMATION_SKELETON = hook("ia", "ac", "Liu;", 1)
COMBATINFO1_HEALTH = hook("do", "ao", "I", 942133651)
COMBATINFO1_HEALTHRATIO = hook("do", "ae", "I", -749589017)
COMBATINFO2_HEALTHSCALE = hook("hl", "ar", "I", 398210675)
COMBATINFOLIST_HEAD = hook("oc", "au", "Lsj;", 1)
COMBATINFOLIST_CURRENT = hook("oc", "ae", "Lsj;", 1)
COMBATINFOHOLDER_COMBATINFOLIST = hook("dm", "at", "Loc;", 1)
COMBATINFOHOLDER_COMBATINFO2 = hook("dm", "ao", "Lhl;", 1)
ACTOR_ANIMATION = hook("dr", "ck", "I", -1553687919)
ACTOR_ANIMATIONDELAY = hook("dr", "dj", "I", 4675371)
ACTOR_ANIMATIONFRAME = hook("dr", "cc", "I", -1662504155)
ACTOR_MOVEMENTSEQUENCE = hook("dr", "cj", "I", -74098563)
ACTOR_MOVEMENTFRAME = hook("dr", "cz", "I", -1996741795)
ACTOR_CURRENTSEQUENCE = hook("dr", "bq", "I", -2115242573)
ACTOR_SPOKENTEXT = hook("dr", "bg", "Ljava/lang/String;", 1)
ACTOR_HITDAMAGES = hook("dr", "cq", "[I", 1)
ACTOR_HITTYPES = hook("dr", "ce", "[I", 1)
ACTOR_HITCYCLE = hook("dr", "cp", "[I", 1)
ACTOR_QUEUEX = hook("dr", "de", "[I", 1)
ACTOR_QUEUEY = hook("dr", "dc", "[I", 1)
ACTOR_QUEUETRAVERSED = hook("dr", "ed", "[Lin;", 1)
ACTOR_QUEUESIZE = hook("dr", "dq", "I", -1388670275)
ACTOR_LOCALX = hook("dr", "bd", "I", 51908093)
ACTOR_LOCALY = hook("dr", "by", "I", 450111749)
ACTOR_COMBATCYCLE = hook("dr", "N/A", "N/A", 1)
ACTOR_INTERACTINGINDEX = hook("dr", "cu", "I", 1926646529)
ACTOR_ORIENTATION = hook("dr", "dp", "I", -609801851)
ACTOR_ISWALKING = hook("dr", "an", "Z", 1)
ACTOR_COMBATINFOLIST = hook("dr", "cl", "Loc;", 1)
ACTOR_SPOTANIMATION = hook("dr", "dy", "I", 1999731983)
ACTOR_SPOTANIMATIONFRAME = hook("N/A", "N/A", "N/A", 1)
ACTOR_SPOTANIMATIONFRAMECYCLE = hook("dr", "dh", "I", 136905603)
ACTOR_GRAPHICSID = hook("N/A", "N/A", "N/A", 1)
ACTOR_HEIGHT = hook("dr", "df", "I", -610695377)
NPCDEFINITION_ID = hook("hw", "ai", "I", -1243106285)
NPCDEFINITION_NAME = hook("hw", "az", "Ljava/lang/String;", 1)
NPCDEFINITION_ACTIONS = hook("hw", "bv", "[Ljava/lang/String;", 1)
NPCDEFINITION_MODELIDS = hook("hw", "aa", "[I", 1)
NPCDEFINITION_COMBATLEVEL = hook("hw", "bd", "I", 989486243)
NPCDEFINITION_VISIBLE = hook("hw", "bm", "Z", 1)
NPCDEFINITION_MODELCACHE = hook("hw", "ac", "Lle;", 1)
NPCDEFINITION_DEFINITIONCACHE = hook("hw", "at", "Lle;", 1)
NPCDEFINITION_TRANSFORMATIONS = hook("hw", "bl", "[I", 1)
NPCDEFINITION_MODELTILESIZE = hook("hw", "ap", "I", -733591527)
NPCDEFINITION_MODELSCALEWIDTH = hook("hw", "by", "I", 1754811063)
NPCDEFINITION_MODELSCALEHEIGHT = hook("hw", "bs", "I", -183655351)
NPCDEFINITION_TRANSFORMVARBIT = hook("hw", "bp", "I", 715362785)
NPCDEFINITION_TRANSFORMVARP = hook("hw", "bu", "I", -541634501)
NPC_DEFINITION = hook("dx", "au", "Lhw;", 1)
PLAYERDEFINITION_NPCTRANSFORMID = hook("mt", "ai", "I", -1253753061)
PLAYERDEFINITION_ISFEMALE = hook("mt", "af", "Z", 1)
PLAYERDEFINITION_ANIMATEDMODELID = hook("mt", "az", "J", -4990962188091480033)
PLAYERDEFINITION_MODELID = hook("mt", "ap", "J", 8032241556888834061)
PLAYERDEFINITION_EQUIPMENT = hook("mt", "ae", "[I", 1)
PLAYERDEFINITION_MODELCACHE = hook("mt", "am", "Lle;", 1)
PLAYER_NAME = hook("df", "au", "Luc;", 1)
PLAYER_MODEL = hook("df", "ab", "Ljr;", 1)
PLAYER_ISHIDDEN = hook("df", "aj", "Z", 1)
PLAYER_DEFINITION = hook("df", "ae", "Lmt;", 1)
PLAYER_COMBATLEVEL = hook("df", "az", "I", 424288465)
PLAYER_INDEX = hook("df", "aw", "I", 1857589841)
PLAYER_ISANIMATING = hook("df", "as", "Z", 1)
PLAYER_OVERHEADPRAYERICON = hook("df", "at", "I", 1489130693)
OBJECTDEFINITION_ID = hook("hv", "aa", "I", 1130646297)
OBJECTDEFINITION_ANIMATIONID = hook("hv", "aw", "I", -671344969)
OBJECTDEFINITION_DEFINITIONCACHE = hook("hv", "at", "Lle;", 1)
OBJECTDEFINITION_MODELCACHE = hook("hv", "az", "Lle;", 1)
OBJECTDEFINITION_MODELIDS = hook("hv", "af", "[I", 1)
OBJECTDEFINITION_MODELS = hook("hv", "ad", "[I", 1)
OBJECTDEFINITION_NAME = hook("hv", "aq", "Ljava/lang/String;", 1)
OBJECTDEFINITION_ACTIONS = hook("hv", "bk", "[Ljava/lang/String;", 1)
OBJECTDEFINITION_TRANSFORMATIONS = hook("hv", "bb", "[I", 1)
OBJECTDEFINITION_TRANSFORMATIONVARBIT = hook("hv", "br", "I", -549604083)
OBJECTDEFINITION_TRANSFORMATIONVARP = hook("hv", "be", "I", 244969535)
PROJECTILE_ID = hook("ck", "au", "I", -549374795)
PROJECTILE_PLANE = hook("ck", "ae", "I", -1311387965)
PROJECTILE_SOURCEX = hook("ck", "ao", "I", -1087687777)
PROJECTILE_SOURCEY = hook("ck", "at", "I", -1807665337)
PROJECTILE_SOURCEZ = hook("ck", "ac", "I", -1307089547)
PROJECTILE_X = hook("ck", "ag", "D", 1)
PROJECTILE_Y = hook("ck", "am", "D", 1)
PROJECTILE_Z = hook("ck", "ax", "D", 1)
PROJECTILE_SPEED = hook("ck", "ay", "D", 1)
PROJECTILE_SPEEDX = hook("ck", "ah", "D", 1)
PROJECTILE_SPEEDY = hook("ck", "as", "D", 1)
PROJECTILE_SPEEDZ = hook("ck", "aj", "D", 1)
PROJECTILE_ACCELERATIONZ = hook("ck", "av", "D", 1)
PROJECTILE_STARTHEIGHT = hook("ck", "al", "I", 48542785)
PROJECTILE_ENDHEIGHT = hook("ck", "ai", "I", -171002147)
PROJECTILE_STARTCYCLE = hook("ck", "af", "I", 1420572405)
PROJECTILE_ENDCYCLE = hook("ck", "ad", "I", 855194403)
PROJECTILE_INTERACTINGINDEX = hook("ck", "ar", "I", -731923483)
PROJECTILE_PITCH = hook("ck", "ak", "I", -600416715)
PROJECTILE_YAW = hook("ck", "aw", "I", -556808089)
PROJECTILE_ISMOVING = hook("ck", "ab", "Z", 1)
PROJECTILE_ANIMATIONFRAME = hook("ck", "bj", "I", 1245655713)
WIDGETNODE_ID = hook("ds", "au", "I", 2086760251)
WIDGET_NAME = hook("mi", "gp", "Ljava/lang/String;", 1)
WIDGET_TEXT = hook("mi", "de", "Ljava/lang/String;", 1)
WIDGET_WIDGETID = hook("mi", "bp", "I", -802277715)
WIDGET_PARENTID = hook("mi", "cr", "I", 1049113007)
WIDGET_PARENT = hook("mi", "ex", "Lmi;", 1)
WIDGET_ITEMID = hook("mi", "gq", "I", 1710253055)
WIDGET_ITEMIDS = hook("mi", "ga", "[I", 1)
WIDGET_STACKSIZES = hook("N/A", "N/A", "N/A", 1)
WIDGET_ITEMAMOUNT = hook("mi", "gt", "I", 1666268347)
WIDGET_SPRITEID = hook("mi", "ct", "I", 1694560891)
WIDGET_TEXTUREID = hook("mi", "cy", "I", -329704335)
WIDGET_MODELID = hook("mi", "dd", "I", -1600832609)
WIDGET_ANIMATIONID = hook("mi", "dy", "I", 1110473721)
WIDGET_ACTIONS = hook("N/A", "N/A", "N/A", 1)
WIDGET_ACTIONTYPE = hook("mi", "bb", "I", 2112192689)
WIDGET_TYPE = hook("mi", "bo", "I", -1370156439)
WIDGET_ISHIDDEN = hook("mi", "cd", "Z", 1)
WIDGET_OPACITY = hook("mi", "cb", "I", -1458216043)
WIDGET_ABSOLUTEX = hook("mi", "bn", "I", 1356456497)
WIDGET_ABSOLUTEY = hook("mi", "bw", "I", -1035953241)
WIDGET_RELATIVEX = hook("mi", "cw", "I", 979552283)
WIDGET_RELATIVEY = hook("mi", "cf", "I", -1112610033)
WIDGET_SCROLLX = hook("mi", "ce", "I", -739875643)
WIDGET_SCROLLY = hook("mi", "cq", "I", 595666453)
WIDGET_WIDTH = hook("mi", "cm", "I", 501302871)
WIDGET_HEIGHT = hook("mi", "cn", "I", 1553685319)
WIDGET_CHILDREN = hook("mi", "gn", "[Lmi;", 1)
WIDGET_BOUNDSINDEX = hook("mi", "hk", "I", 1527386271)
WIDGET_WIDGETCYCLE = hook("mi", "hz", "I", -822322021)
ITEMDEFINITION_ID = hook("hn", "an", "I", -466945669)
ITEMDEFINITION_NAME = hook("hn", "ab", "Ljava/lang/String;", 1)
ITEMDEFINITION_ISMEMBERS = hook("hn", "bs", "Z", 1)
ITEMDEFINITION_GROUNDACTIONS = hook("hn", "bm", "[Ljava/lang/String;", 1)
ITEMDEFINITION_ACTIONS = hook("hn", "bf", "[Ljava/lang/String;", 1)
ITEMDEFINITION_CACHE = hook("hn", "af", "Lle;", 1)
ITEM_ID = hook("ed", "au", "I", 943663449)
ITEM_STACKSIZES = hook("ed", "ae", "I", -2002661055)
ITEMNODE_ITEMIDS = hook("dd", "ae", "[I", 1)
ITEMNODE_ITEMQUANTITIES = hook("dd", "ao", "[I", 1)
ITEMNODE_CACHE = hook("dd", "au", "Lso;", 1)
LOGIN_XPADDING = hook("cy", "ao", "I", 657439907)
LOGIN_BOXXOFFSET = hook("cy", "ay", "I", -390756021)
LOGIN_LOADINGPERCENT = hook("cy", "av", "I", -427966603)
LOGIN_ACCOUNTSTATUS = hook("cy", "bi", "I", -1116009889)
LOGIN_INDEX = hook("cy", "cw", "I", 1467944731)
LOGIN_BUTTONSPRITE = hook("it", "ai", "Luk;", 1)
LOGIN_USERNAME = hook("cy", "cx", "Ljava/lang/String;", 1)
LOGIN_PASSWORD = hook("cy", "cr", "Ljava/lang/String;", 1)
LOGIN_CURSORFIELD = hook("cy", "dh", "I", -1433824975)
VARPS_MASKS = hook("mz", "au", "[I", 1)
VARPS_MAIN = hook("mz", "ao", "[I", 1)
VARCS_MAP = hook("ej", "at", "Ljava/util/Map;", 1)
VARCS_STRINGS = hook("ej", "ac", "[Ljava/lang/String;", 1)
VARCS_VARCMAP = hook("ej", "at", "Ljava/util/Map;", 1)
VARBITDEFINITION_CACHE = hook("hb", "ae", "Lle;", 1)
VARBITDEFINITION_BASE = hook("hb", "ao", "I", 144903653)
VARBITDEFINITION_STARTBIT = hook("hb", "at", "I", 225410143)
VARBITDEFINITION_ENDBIT = hook("hb", "ac", "I", 1882806955)
CLIENT_REVISION = hook("uy", "ao", "I", -671342643)
CLIENT_CLIENT = hook("it", "bw", "Lclient;", 1)
CLIENT_LOCALNPCS = hook("client", "ij", "[Ldx;", 1)
CLIENT_NPCINDICES = hook("client", "ih", "[I", 1)
CLIENT_NPCCOUNT = hook("client", "in", "I", 641541081)
CLIENT_LOCALPLAYERS = hook("client", "mi", "[Ldf;", 1)
CLIENT_PLAYERINDICES = hook("ee", "az", "[I", 1)
CLIENT_PLAYERCOUNT = hook("ee", "ai", "I", 2110833449)
CLIENT_LOCALPLAYER = hook("hb", "mo", "Ldf;", 1)
CLIENT_PLAYERINDEX = hook("client", "mx", "I", 530420265)
CLIENT_LOOPCYCLE = hook("client", "eh", "I", 522278027)
CLIENT_GAMESTATE = hook("client", "dj", "I", -667400491)
CLIENT_LOGINSTATE = hook("client", "gi", "I", 1808720373)
CLIENT_ISLOADING = hook("N/A", "N/A", "N/A", 1)
CLIENT_CROSSHAIRCOLOR = hook("client", "mj", "I", 1950062223)
CLIENT_ANIMATIONFRAMECACHE = hook("ib", "aa", "Lle;", 1)
CLIENT_GROUNDITEMS = hook("client", "nr", "[[[Low;", 1)
CLIENT_COLLISIONMAPS = hook("client", "jz", "[Lis;", 1)
CLIENT_PROJECTILES = hook("client", "nn", "Low;", 1)
CLIENT_GRAPHICSOBJECTS = hook("client", "nw", "Low;", 1)
CLIENT_GRANDEXCHANGEOFFERS = hook("client", "wf", "[Loh;", 1)
CLIENT_CAMERAX = hook("hw", "kk", "I", 757716957)
CLIENT_CAMERAY = hook("fr", "km", "I", 1907020251)
CLIENT_CAMERAZ = hook("fl", "kc", "I", 912731593)
CLIENT_CAMERAPITCH = hook("ep", "kz", "I", 1065394883)
CLIENT_CAMERAYAW = hook("ef", "kh", "I", 1799410691)
CLIENT_REGION = hook("fh", "jb", "Liv;", 1)
CLIENT_ISREGIONINSTANCED = hook("client", "jp", "Z", 1)
CLIENT_REGIONINSTANCES = hook("N/A", "N/A", "N/A", 1)
CLIENT_PLANE = hook("dm", "mn", "I", 1873768041)
CLIENT_BASEX = hook("ev", "je", "I", 1638537919)
CLIENT_BASEY = hook("bx", "jr", "I", 1819265849)
CLIENT_DESTINATIONX = hook("client", "tz", "I", 850793817)
CLIENT_DESTINATIONY = hook("client", "ti", "I", -214324647)
CLIENT_SINE = hook("ix", "at", "[I", 1)
CLIENT_COSINE = hook("ix", "ac", "[I", 1)
CLIENT_TILEHEIGHTS = hook("du", "au", "[[[I", 1)
CLIENT_TILESETTINGS = hook("du", "ae", "[[[B", 1)
CLIENT_ITEMNODECACHE = hook("dd", "au", "Lso;", 1)
CLIENT_WIDGETS = hook("ly", "ak", "[[Lmi;", 1)
CLIENT_GAMESETTINGS = hook("mz", "ao", "[I", 1)
CLIENT_WIDGETNODECACHE = hook("client", "pu", "Lso;", 1)
CLIENT_WIDGETPOSITIONX = hook("client", "rt", "[I", 1)
CLIENT_WIDGETPOSITIONY = hook("client", "rx", "[I", 1)
CLIENT_WIDGETWIDTHS = hook("client", "rw", "[I", 1)
CLIENT_WIDGETHEIGHTS = hook("client", "rn", "[I", 1)
CLIENT_VALIDWIDGETS = hook("mq", "bh", "[Z", 1)
CLIENT_WIDGETROOTINTERFACE = hook("client", "pj", "I", 1642683045)
CLIENT_VIEWPORTWIDTH = hook("client", "vo", "I", -685574095)
CLIENT_VIEWPORTHEIGHT = hook("client", "vn", "I", -212965565)
CLIENT_VIEWPORTSCALE = hook("client", "vx", "I", -544120667)
CLIENT_MAPANGLE = hook("client", "lx", "I", -817936455)
CLIENT_MAPSCALE = hook("N/A", "N/A", "N/A", 1)
CLIENT_MAPOFFSET = hook("N/A", "N/A", "N/A", 1)
CLIENT_MENUCOUNT = hook("client", "om", "I", 1676985473)
CLIENT_MENUACTIONS = hook("client", "ob", "[Ljava/lang/String;", 1)
CLIENT_MENUOPTIONS = hook("client", "ok", "[Ljava/lang/String;", 1)
CLIENT_ISMENUOPEN = hook("client", "nf", "Z", 1)
CLIENT_MENUX = hook("al", "no", "I", 457066205)
CLIENT_MENUY = hook("qf", "nx", "I", 183418913)
CLIENT_MENUWIDTH = hook("mq", "nh", "I", 617707969)
CLIENT_MENUHEIGHT = hook("jn", "nc", "I", 1693604393)
CLIENT_ISRESIZABLE = hook("client", "sd", "Z", 1)
CLIENT_CURRENTLEVELS = hook("client", "ny", "[I", 1)
CLIENT_REALLEVELS = hook("client", "nk", "[I", 1)
CLIENT_EXPERIENCES = hook("client", "nj", "[I", 1)
CLIENT_CURRENTWORLD = hook("client", "bg", "I", -831561099)
CLIENT_ENERGY = hook("client", "px", "I", 2106479597)
CLIENT_WEIGHT = hook("client", "pt", "I", 679999119)
CLIENT_ISITEMSELECTED = hook("client", "ov", "I", 61632949)
CLIENT_ISSPELLSELECTED = hook("client", "or", "Z", 1)
