import math
import time

import engine
from engine.events import *
from engine.operators import *
from engine.types import *


@sprite('Stage')
class Stage(Target):
    """Sprite Stage"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "None", [
            {
                'name': "backdrop2",
                'path': "e2f51e475b5ae5eb2ada7a9b444fe10f.png",
                'center': (480, 360),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_PLAYERX = 0
        self.var_PLAYERY = 21
        self.var_CAMERAX = 0
        self.var_CAMERAY = 44
        self.var_PLAYERSX = 0
        self.var_PLAYERSY = -0.9284505212495042
        self.var_HAMMERX = -77.35652729741759
        self.var_HAMMERY = 86.27987394275495
        self.var_MAXLEN = 102
        self.var_HAMMERMX = 56392.32535333979
        self.var_HAMMERMY = -2093.8524822644436
        self.var_HAMMERAIR = 183
        self.var_FRAME = 1543
        self.var_DEBUG = "11"
        self.var_MINLEN = 26
        self.var_BRIGHT = 314
        self.var_SFX = "true"
        self.var_COMMENTARY = "true"
        self.var_FASTEST = 1543
        self.var_LATEST = 8301
        self.var_cloudlist1 = 5429271820146363656765690041543481828126364656600416162812271029121763260041683391031182865680041716431027273476512429291427340041818365756112724280041819382718222824237348101421282927242200418486966536667004184927142328640041899646810311427341900419971127
        self.var_cloudlist2 = 3023241332182211100042039112411102210151828170042077111829122413146362620042102431027273476103114273419004212043102727347610311427341900421203817182576401029142776636465004212922715232124311427640214241407650151518121810210042198541227102912171427372434350
        self.var_cloudlist3 = "042235733818221423102918127300422364026390042250132218292734636465640042290551714382421101114270042294122118122014271624231428004231523242373161423142718122800423256642646263700042340"
        self.var_cloudlist4 = ""
        self.var_cloudlist5 = ""
        self.var_cloudlist6 = ""
        self.var_cloudlist7 = ""
        self.var_cloudlock = 9235639673

        self.list_Hands = List(
            [-8, -14.361991533512601, -26.5668515549157, 8, -14.361991533512601, -32.67996045735016]
        )
        self.list_HandsY = List(
            [-24, 185.0974005650802, -0.5734369990971118, -24, 185.0974005650802, 4.586979606854054]
        )
        self.list_DEBUG = List(
            []
        )
        self.list_TIME = List(
            [1, 5, 0]
        )
        self.list_CLOUDLIST = List(
            ["Strike113537", 1543, "Misc1234", 1616, "scratch1q", 1683, "Davis36", 1716, "Harry_Pottery", 1818, "AVUbros", 1819, "Crimson-Maelstrom", 1848, "74R45", 1849, "rens2", 1899, "26averyj", 1997, "brunodwimba", 2039, "bobamafish", 2077, "bitcode100", 2102, "Harry_averyj", 2120, "Harry_averyj", 2120, "Chip_Eater_123", 2129, "m9QwcHbG_ElGFE_Official", 2198, "ScratcherBoyz", 2235, "-Cimenatic-", 2236, "EqD", 2250, "dmitry1232", 2290, "TheColaber", 2294, "clickergones", 2315, "non-generics", 2325, "4G2018", 2340]
        )

        self.sprite.layer = 0

    @on_broadcast('position level')
    async def broadcast_PositionLevel(self, util):
        await self.my_bright(util, toint((315 - div(self.var_CAMERAY, 30))))

    async def my_bright(self, util, arg_level):
        if not eq(arg_level, self.var_BRIGHT):
            self.var_BRIGHT = arg_level
            self.costume.set_effect('brightness', arg_level)


@sprite('Blank')
class SpriteBlank(Target):
    """Sprite Blank"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "costume1",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])





        self.sprite.layer = 6

    @on_green_flag
    async def green_flag(self, util):
        self.gotoxy(0, 0)


@sprite('Player')
class SpritePlayer(Target):
    """Sprite Player"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = -23
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           2, 100, "all around", [
            {
                'name': "player hitbox",
                'path': "52680cf0b5f2904c4bda629bec95dcea.svg",
                'center': (10, 12),
                'scale': 1
            },
            {
                'name': "hammer hitbox",
                'path': "0a365f2c0fe1ae815645642d7004fb6e.png",
                'center': (8, 8),
                'scale': 2
            },
            {
                'name': "player",
                'path': "da987a59a8be86f9ca2460ecd0be30ce.svg",
                'center': (19, 6),
                'scale': 1
            },
            {
                'name': "player2",
                'path': "3d42cd040dc35903477956241fc031f6.svg",
                'center': (25, 36),
                'scale': 1
            },
            {
                'name': "big",
                'path': "c4a7b162c46837444e865d00a9da0bc0.svg",
                'center': (194, 137),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            50, [
            {
                'name': "newclunk1",
                'path': "8f7d0e6e840fc92a2915d5bb70720ff0.wav"
            },
            {
                'name': "newclunk2",
                'path': "7bc73cb26b60c9860dab3add25403531.wav"
            },
            {
                'name': "newclunk3",
                'path': "c427562d7e519e91159ce4048fa58538.wav"
            },
            {
                'name': "newclunk4",
                'path': "2f668d522449f216a0b942c52b586a78.wav"
            },
            {
                'name': "newclunk5",
                'path': "74eb99666ada2c967d5f33a82ad1c5df.wav"
            },
            {
                'name': "jump1",
                'path': "82a9ca4a00e9d512b6e1a05de04c5f82.wav"
            },
            {
                'name': "jump2",
                'path': "ee3313dad93b6e523668d93f668788ac.wav"
            },
            {
                'name': "jump3",
                'path': "a64601c503279233653704bbd1d75cff.wav"
            },
            {
                'name': "jump4",
                'path': "e95f520bd05e99a32aed117ef6e31dd4.wav"
            },
            {
                'name': "jump5",
                'path': "49930b9aec4a40939479bb774be63e19.wav"
            },
            {
                'name': "whu1",
                'path': "2eb3d1870dab4d6a13a4821cb1c54e25.wav"
            },
            {
                'name': "whu2",
                'path': "4e3d603c3d37d052da090fe4643555bc.wav"
            },
            {
                'name': "whu3",
                'path': "a2002bdedb8dcfd5bd04054eec57bf63.wav"
            },
            {
                'name': "whu4",
                'path': "1a2abf491f804d2f5f7ec6457bc036e7.wav"
            },
            {
                'name': "whu5",
                'path': "c2030e02dbc29a280eb6a15892026657.wav"
            },
            {
                'name': "whu6",
                'path': "64f572adbb5be439e57f68ea32207c6d.wav"
            },
            {
                'name': "newscrape1",
                'path': "6049d5c62ca55d2999ade5dee1d5027f.wav"
            },
            {
                'name': "newscrape2",
                'path': "0f26ddf41645101547cb58d6ca257834.wav"
            },
            {
                'name': "newscrape3",
                'path': "32c52c6355ee7c59286f9a49939f06d2.wav"
            },
            {
                'name': "newscrape4",
                'path': "1d0e65391d992b44a528dce138edbad9.wav"
            },
            {
                'name': "newscrape5",
                'path': "964cbf3411c3fbda64b15b3250aa3446.wav"
            },
            {
                'name': "Small_Splash_Audio",
                'path': "96a0cb2fb25605839cd81466e4717a87.wav"
            },
            {
                'name': "hit_fabricb_1",
                'path': "a020d433f39c468a74466bd26d9d0375.wav"
            },
            {
                'name': "hit_fabricb_2",
                'path': "00cd5394b304c22bb432aca0e85471b3.wav"
            },
            {
                'name': "hit_fabricb_3",
                'path': "9f84216d2635f7edff916ba1c300dc04.wav"
            },
            {
                'name': "hit_fabricb_4",
                'path': "383a343429872cc16dd73ea2937c3346.wav"
            },
            {
                'name': "hit_fabricb_5",
                'path': "8f03ae864c020f4be15e9eb9767d6413.wav"
            },
            {
                'name': "hardhit_fabricb_1",
                'path': "ab1fc2ccbe78a5d437b57c3d79271d37.wav"
            },
            {
                'name': "hardhit_fabricb_2",
                'path': "faa7039a301789a34484cd398fcb0fd8.wav"
            },
            {
                'name': "hardhit_fabricb_4",
                'path': "9ad56d0694b49ebd261d17073b4175c6.wav"
            },
            {
                'name': "hardhit_fabricb_5",
                'path': "8376613fddcb527ac385b1ca7789fcb1.wav"
            },
            {
                'name': "scrape_plastic_1",
                'path': "954cc3b716d4f5a95bc8ea560ccd32a5.wav"
            },
            {
                'name': "scrape_plastic_2",
                'path': "b2f1719d9050c65404c26275ad9bdb2c.wav"
            },
            {
                'name': "scrape_plastic_3",
                'path': "5e1c3f6a3fa8ac4d260a7502444cb0ec.wav"
            },
            {
                'name': "scrape_plastic_4",
                'path': "5a93a29a75772c5c6648063a95e54f47.wav"
            }
        ])

        self.var_distance = 0.7244456913222792
        self.var_touch = 0
        self.var_tx = 0
        self.var_ty = 21
        self.var_ox = 0
        self.var_oy = 21
        self.var_t = 0
        self.var_dx = 0
        self.var_dy = -0.9284505212495042
        self.var_lasttx = -61.88079347404203
        self.var_lastty = 53.59921883886341
        self.var_lastmousex = -232
        self.var_lastmousey = 180
        self.var_touchx = "1.0807323842708525e-09"
        self.var_touchy = "2.6038381360287455e-09"
        self.varcamerax = 0
        self.varcameray = 43.91981302799999
        self.var_d2 = 1.8569010424990084
        self.var_sensePX = 0
        self.var_sensePY = 21
        self.var_sensePV = "False"
        self.var_sameHX = -77
        self.var_sameHY = 86
        self.var_sameHV = "False"
        self.var_lastEffort = "0"
        self.var_effort = "0.15589537533260675"
        self.var_ax = 0
        self.var_hvy = -1.4441579201730876
        self.var_lastHx = -77.29801631489495
        self.var_lastHy = 87.00195290284148
        self.var_lasthdist = 0.7244456913222792
        self.var_cox = 0
        self.var_coy = 20
        self.var_lasttouch = 0
        self.var_ContactY = 21

        self.list_fix = StaticList(
            [0, 1, -1, -1, 2, 0, 0, 1, -2, 0, 1, -2, -1, 0, 2, 0, -1, 2]
        )
        self.list_planet = List(
            [4456, 12795, 3662, 13475, 5069, 13840, 4171, 14109, 3270, 14508, 3741, 14839, 4718, 14744]
        )

        self.sprite.layer = 9

    @on_broadcast('tick player')
    async def broadcast_tickplayer(self, util):
        if (util.inputs["w"] and eq(config.USERNAME, "griffpatch")):
            util.sprites.stage.var_PLAYERSX = div(util.inputs.mouse_x, 7)
            util.sprites.stage.var_PLAYERSY = div(util.inputs.mouse_y, 7)
        await self.my_tick(util, )
        await self.my_tGetScroll(util, ((util.sprites.stage.var_PLAYERX + self.var_cox) - self.varcamerax), 1500, 40)
        self.varcamerax += self.var_t
        await self.my_tGetScroll(util, ((util.sprites.stage.var_PLAYERY + self.var_coy) - self.varcameray), 1500, 40)
        self.varcameray += self.var_t
        util.sprites.stage.var_CAMERAX = toint(self.varcamerax)
        util.sprites.stage.var_CAMERAY = toint(self.varcameray)
        if lt(util.sprites.stage.var_CAMERAY, 0):
            util.sprites.stage.var_CAMERAY = 0
        self.costume.switch("big")
        self.gotoxy((util.sprites.stage.var_PLAYERX - util.sprites.stage.var_CAMERAX), (util.sprites.stage.var_PLAYERY - util.sprites.stage.var_CAMERAY))
        self.costume.switch("player")

    @warp
    async def my_tick(self, util, ):
        self.var_lastHx = util.sprites.stage.var_HAMMERX
        self.var_lastHy = util.sprites.stage.var_HAMMERY
        self.var_sensePX = 0
        await self.my_Gravity(util, )
        if lt(util.sprites.stage.var_PLAYERX, -1000):
            util.sprites.stage.var_PLAYERX = -1000
        if gt(util.sprites.stage.var_PLAYERX, 5480):
            util.sprites.stage.var_PLAYERX = 5480
        if lt(util.sprites.stage.var_PLAYERSY, -64):
            util.sprites.stage.var_PLAYERSY = -64
        await self.my_position(util, )
        self.var_tx = (0.4 * (util.inputs.mouse_x - (util.sprites.stage.var_HAMMERX - (util.sprites.stage.var_PLAYERX + self.var_cox))))
        self.var_ty = (0.4 * (util.inputs.mouse_y - (util.sprites.stage.var_HAMMERY - (util.sprites.stage.var_PLAYERY + self.var_coy))))
        self.var_touchx = str((tonum(self.var_touchx) * 0.85))
        self.var_touchy = str((tonum(self.var_touchy) * 0.85))
        self.var_lastmousex = util.inputs.mouse_x
        self.var_lastmousey = util.inputs.mouse_y
        await self.my_distance(util, (self.var_tx - self.var_lasttx), (self.var_ty - self.var_lastty))
        if gt(self.var_distance, 40):
            self.var_tx = (div((self.var_tx - self.var_lasttx), div(self.var_distance, 40)) + self.var_lasttx)
            self.var_ty = (div((self.var_ty - self.var_lastty), div(self.var_distance, 40)) + self.var_lastty)
        self.var_effort = str(self.var_distance)
        self.var_lasttx = self.var_tx
        self.var_lastty = self.var_ty
        await self.my_distance(util, self.var_tx, self.var_ty)
        if gt(self.var_distance, 50):
            self.var_tx = div(self.var_tx, div(self.var_distance, 50))
            self.var_ty = div(self.var_ty, div(self.var_distance, 50))
        await self.my_Extent(util, ((util.sprites.stage.var_HAMMERX + self.var_tx) - util.sprites.stage.var_PLAYERX), ((util.sprites.stage.var_HAMMERY + self.var_ty) - util.sprites.stage.var_PLAYERY))
        await self.my_distance(util, self.var_tx, self.var_ty)
        self.var_t = self.var_distance
        await self.my_distance(util, (util.sprites.stage.var_PLAYERSX + self.var_tx), (util.sprites.stage.var_PLAYERSY + self.var_ty))
        if gt(self.var_t, self.var_distance):
            self.var_distance = self.var_t
        if lt(self.var_distance, 1):
            self.var_distance = 1
        else:
            self.var_distance = math.ceil(self.var_distance)
        self.var_dx = div(util.sprites.stage.var_PLAYERSX, self.var_distance)
        self.var_dy = div(util.sprites.stage.var_PLAYERSY, self.var_distance)
        self.var_hvy = (util.sprites.stage.var_PLAYERSY + self.var_ty)
        await self.my_movehammer(util, div(self.var_tx, self.var_distance), div(self.var_ty, self.var_distance), self.var_distance)
        await self.my_distance(util, (util.sprites.stage.var_HAMMERX - self.var_lastHx), (util.sprites.stage.var_HAMMERY - self.var_lastHy))
        self.var_lasthdist = self.var_distance

    @warp
    async def my_position(self, util, ):
        self.gotoxy((util.sprites.stage.var_PLAYERX - util.sprites.stage.var_CAMERAX), (util.sprites.stage.var_PLAYERY - util.sprites.stage.var_CAMERAY))

    @warp
    async def my_distance(self, util, arg_dx, arg_dy):
        self.var_distance = sqrt(((tonum(arg_dx) * tonum(arg_dx)) + (tonum(arg_dy) * tonum(arg_dy))))

    @warp
    async def my_touchtouching(self, util, arg_player, arg_hammer):
        if arg_hammer:
            if (eq(toint(util.sprites.stage.var_HAMMERX), self.var_sameHX) and eq(toint(util.sprites.stage.var_HAMMERY), self.var_sameHY)):
                pass
            else:
                self.costume.switch("hammer hitbox")
                self.gotoxy((util.sprites.stage.var_HAMMERX - util.sprites.stage.var_CAMERAX), (util.sprites.stage.var_HAMMERY - util.sprites.stage.var_CAMERAY))
                self.var_sameHV = str(self.get_touching(util, "Level"))
                self.var_sameHX = toint(util.sprites.stage.var_HAMMERX)
                self.var_sameHY = toint(util.sprites.stage.var_HAMMERY)
            if self.get_touching(util, "Level"):
                self.var_touch = 1
                return None
        if arg_player:
            if (eq(toint(util.sprites.stage.var_PLAYERX), self.var_sensePX) and eq(toint(util.sprites.stage.var_PLAYERY), self.var_sensePY)):
                pass
            else:
                self.costume.switch("player hitbox")
                self.gotoxy((util.sprites.stage.var_PLAYERX - util.sprites.stage.var_CAMERAX), (util.sprites.stage.var_PLAYERY - util.sprites.stage.var_CAMERAY))
                self.var_sensePV = str(self.get_touching(util, "Level"))
                self.var_sensePX = toint(util.sprites.stage.var_PLAYERX)
                self.var_sensePY = toint(util.sprites.stage.var_PLAYERY)
            if eq(self.var_sensePV, "true"):
                self.var_touch = 2
                return None
        self.var_touch = 0

    @on_broadcast('fix collisions')
    async def broadcast_fixcollisions(self, util):
        await self.my_fixplayer(util, )
        await self.my_fixhammer(util, )

    @warp
    async def my_Extent(self, util, arg_dx, arg_dy):
        await self.my_distance(util, arg_dx, arg_dy)
        if gt(self.var_distance, util.sprites.stage.var_MAXLEN):
            self.var_tx += ((div(arg_dx, self.var_distance) * util.sprites.stage.var_MAXLEN) - arg_dx)
            self.var_ty += ((div(arg_dy, self.var_distance) * util.sprites.stage.var_MAXLEN) - arg_dy)
        if lt(self.var_distance, util.sprites.stage.var_MINLEN):
            self.var_tx += ((div(arg_dx, self.var_distance) * util.sprites.stage.var_MINLEN) - arg_dx)
            self.var_ty += ((div(arg_dy, self.var_distance) * util.sprites.stage.var_MINLEN) - arg_dy)

    @warp
    async def my_movehammer(self, util, arg_dx, arg_dy, arg_distance):
        self.var_ox = util.sprites.stage.var_PLAYERX
        self.var_oy = util.sprites.stage.var_PLAYERY
        if lt(self.var_lasthdist, 3):
            self.var_tx = util.sprites.stage.var_HAMMERX
            self.var_ty = util.sprites.stage.var_HAMMERY
            await self.my_hammerwall(util, (arg_dx + div(util.sprites.stage.var_PLAYERSX, arg_distance)), (arg_dy + div(util.sprites.stage.var_PLAYERSY, arg_distance)))
            util.sprites.stage.var_HAMMERX = self.var_tx
            util.sprites.stage.var_HAMMERY = self.var_ty
        else:
            self.var_touch = 0
        if gt(self.var_touch, 0):
            await self.my_moveplayernext(util, (-0.5 * arg_dx), (-0.5 * arg_dy))
        else:
            await self.my_movehammerfirst(util, arg_dx, arg_dy, util.sprites.stage.var_PLAYERSX, util.sprites.stage.var_PLAYERSY)
        if (lt(util.sprites.stage.var_PLAYERY, -43) and not lt(self.var_oy, -43)):
            self.sounds.play("Small_Splash_Audio")

    @warp
    async def my_momentum(self, util, arg_dx, arg_dy):
        await self.my_distance(util, (util.sprites.stage.var_HAMMERX - util.sprites.stage.var_PLAYERX), (util.sprites.stage.var_HAMMERY - util.sprites.stage.var_PLAYERY))
        self.var_t = div((util.sprites.stage.var_HAMMERY - util.sprites.stage.var_PLAYERY), self.var_distance)
        if lt(self.var_t, -0.75):
            util.sprites.stage.var_PLAYERSX += (1 * (arg_dx - util.sprites.stage.var_PLAYERSX))
            util.sprites.stage.var_PLAYERSY += (1 * (arg_dy - util.sprites.stage.var_PLAYERSY))
        else:
            util.sprites.stage.var_PLAYERSX += (0.77 * (arg_dx - util.sprites.stage.var_PLAYERSX))
            util.sprites.stage.var_PLAYERSY += (0.77 * (arg_dy - util.sprites.stage.var_PLAYERSY))

    @warp
    async def my_moveplayernext(self, util, arg_dx, arg_dy):
        if False:
            self.var_ox += (0.5 * (util.sprites.stage.var_PLAYERX - self.var_ox))
            self.var_ox += (0.5 * (util.sprites.stage.var_PLAYERY - self.var_oy))
        if gt(util.sprites.stage.var_HAMMERAIR, 0):
            self.var_touchx = str((0 - (util.inputs.mouse_x - (util.sprites.stage.var_HAMMERX - util.sprites.stage.var_PLAYERX))))
            self.var_touchy = str((0 - (util.inputs.mouse_y - (util.sprites.stage.var_HAMMERY - util.sprites.stage.var_PLAYERY))))
            util.sprites.stage.var_HAMMERAIR = 0
        for _ in range(toint(self.var_distance)):
            self.var_tx = util.sprites.stage.var_PLAYERX
            self.var_ty = util.sprites.stage.var_PLAYERY
            util.sprites.stage.var_PLAYERX += arg_dx
            util.sprites.stage.var_PLAYERX += self.var_dx
            await self.my_touchtouching(util, not False, False)
            if gt(self.var_touch, 0):
                util.sprites.stage.var_PLAYERX = self.var_tx
                util.sprites.stage.var_PLAYERSX = 0
                self.var_dx = 0
            util.sprites.stage.var_PLAYERY += arg_dy
            util.sprites.stage.var_PLAYERY += self.var_dy
            await self.my_touchtouching(util, not False, False)
            if gt(self.var_touch, 0):
                util.sprites.stage.var_PLAYERY = self.var_ty
                util.sprites.stage.var_PLAYERSY = 0
                self.var_dy = 0
            if False:
                self.var_tx = util.sprites.stage.var_HAMMERX
                self.var_ty = util.sprites.stage.var_HAMMERY
                util.sprites.stage.var_HAMMERX += self.var_dx
                util.sprites.stage.var_HAMMERY += self.var_dy
                await self.my_touchtouching(util, False, not False)
                if gt(self.var_touch, 0):
                    util.sprites.stage.var_HAMMERX = self.var_tx
                    util.sprites.stage.var_HAMMERY = self.var_ty
        await self.my_momentum(util, (0.55 * (util.sprites.stage.var_PLAYERX - self.var_ox)), ((0.55 * (util.sprites.stage.var_PLAYERY - self.var_oy)) + 0))

    @warp
    async def my_movehammerfirst(self, util, arg_dx, arg_dy, arg_lpsx, arg_lpsy):
        while not lt(self.var_distance, 1):
            await self.my_hammertick(util, arg_dx, arg_dy, util.sprites.stage.var_HAMMERX, util.sprites.stage.var_HAMMERY, arg_lpsx, arg_lpsy)
            self.var_distance += -1
        util.sprites.stage.var_HAMMERAIR += 1

    @warp
    async def my_fixplayer(self, util, ):
        await self.my_touchtouching(util, not False, False)
        if eq(self.var_touch, 0):
            return None
        self.var_t = 1
        for _ in range(8):
            util.sprites.stage.var_PLAYERX += tonum(self.list_fix[toint(self.var_t)])
            self.var_t += 1
            util.sprites.stage.var_PLAYERY += tonum(self.list_fix[toint(self.var_t)])
            self.var_t += 1
            await self.my_touchtouching(util, not False, False)
            if eq(self.var_touch, 0):
                return None
        util.sprites.stage.var_PLAYERX += tonum(self.list_fix[toint(self.var_t)])
        self.var_t += 1
        util.sprites.stage.var_PLAYERY += tonum(self.list_fix[toint(self.var_t)])
        self.var_t = 1
        for _ in range(8):
            util.sprites.stage.var_PLAYERX += (tonum(self.list_fix[toint(self.var_t)]) * 2)
            self.var_t += 1
            util.sprites.stage.var_PLAYERY += (tonum(self.list_fix[toint(self.var_t)]) * 2)
            self.var_t += 1
            await self.my_touchtouching(util, not False, False)
            if eq(self.var_touch, 0):
                return None
        util.sprites.stage.var_PLAYERX += (tonum(self.list_fix[toint(self.var_t)]) * 2)
        self.var_t += 1
        util.sprites.stage.var_PLAYERY += ((tonum(self.list_fix[toint(self.var_t)]) * 2) - 1)

    @warp
    async def my_fixhammer(self, util, ):
        await self.my_touchtouching(util, False, not False)
        if eq(self.var_touch, 0):
            return None
        self.var_t = 1
        for _ in range(8):
            util.sprites.stage.var_HAMMERX += tonum(self.list_fix[toint(self.var_t)])
            self.var_t += 1
            util.sprites.stage.var_HAMMERY += tonum(self.list_fix[toint(self.var_t)])
            self.var_t += 1
            await self.my_touchtouching(util, False, not False)
            if eq(self.var_touch, 0):
                return None
        util.sprites.stage.var_HAMMERX += tonum(self.list_fix[toint(self.var_t)])
        self.var_t += 1
        util.sprites.stage.var_HAMMERY += (tonum(self.list_fix[toint(self.var_t)]) - 1)
        self.var_t = 1
        for _ in range(8):
            util.sprites.stage.var_HAMMERX += (tonum(self.list_fix[toint(self.var_t)]) * 2)
            self.var_t += 1
            util.sprites.stage.var_HAMMERY += (tonum(self.list_fix[toint(self.var_t)]) * 2)
            self.var_t += 1
            await self.my_touchtouching(util, False, not False)
            if eq(self.var_touch, 0):
                return None
        util.sprites.stage.var_HAMMERX += (tonum(self.list_fix[toint(self.var_t)]) * 2)
        self.var_t += 1
        util.sprites.stage.var_HAMMERY += ((tonum(self.list_fix[toint(self.var_t)]) * 2) - 1)

    @warp
    async def my_hammerwall(self, util, arg_dx, arg_dy):
        self.var_t = sqrt(((arg_dx * arg_dx) + (arg_dy * arg_dy)))
        if gt(abs(div(arg_dx, self.var_t)), 0.2):
            util.sprites.stage.var_HAMMERX += div(arg_dx, abs(arg_dx))
        if gt(abs(div(arg_dy, self.var_t)), 0.2):
            util.sprites.stage.var_HAMMERY += div(arg_dy, abs(arg_dy))
        await self.my_touchtouching(util, False, not False)
        if gt(self.var_touch, 0):
            if (gt(self.var_effort, 17) and lt(self.var_lastEffort, 18)):
                if gt(abs((util.sprites.stage.var_HAMMERX - util.sprites.stage.var_PLAYERX)), 40):
                    self.sounds.play(("whu" + str(pick_rand(1, 6))))
                else:
                    self.sounds.play(("jump" + str(pick_rand(1, 5))))
                self.var_lastEffort = self.var_effort
        else:
            if lt(self.var_effort, 5):
                self.var_lastEffort = "0"

    @warp
    async def my_tGetScroll(self, util, arg_d, arg_divide, arg_cap):
        if gt(abs(arg_d), 3):
            self.var_tx = div((abs(arg_d) + 25), arg_divide)
            if gt(self.var_tx, 1):
                self.var_t = (arg_d * 1)
            else:
                self.var_t = (arg_d * self.var_tx)
            if gt(abs(self.var_t), arg_cap):
                self.var_t = (arg_cap * div(self.var_t, abs(self.var_t)))
            self.var_t = (arg_cap * math.sin(math.radians((div(abs(self.var_t), arg_cap) * 90))))
            if lt(arg_d, 0):
                self.var_t = (0 - self.var_t)
        else:
            self.var_t = 0

    @warp
    async def my_hammertick(self, util, arg_dx, arg_dy, arg_hx, arg_hy, arg_lpsx, arg_lpsy):
        self.var_tx = util.sprites.stage.var_HAMMERX
        self.var_ty = util.sprites.stage.var_HAMMERY
        util.sprites.stage.var_HAMMERX += tonum(arg_dx)
        util.sprites.stage.var_HAMMERY += tonum(arg_dy)
        util.sprites.stage.var_HAMMERX += self.var_dx
        util.sprites.stage.var_HAMMERY += self.var_dy
        self.var_ax = 0
        await self.my_touchtouching(util, False, not False)
        if gt(self.var_touch, 0):
            util.sprites.stage.var_HAMMERX += -1
            await self.my_touchtouching(util, False, not False)
            if gt(self.var_touch, 0):
                util.sprites.stage.var_HAMMERX += 2
                await self.my_touchtouching(util, False, not False)
                if gt(self.var_touch, 0):
                    await self.my_lastcontact(util, )
                    if gt(self.var_effort, 10):
                        if gt(util.sprites.stage.var_FRAME, self.var_lasttouch):
                            self.sounds.play(("hardhit_fabricb_" + str(pick_rand(1, 4))))
                            self.var_lasttouch = (util.sprites.stage.var_FRAME + 5)
                    else:
                        if gt(self.var_effort, 2):
                            if gt(util.sprites.stage.var_FRAME, self.var_lasttouch):
                                self.sounds.play(("hit_fabricb_" + str(pick_rand(1, 5))))
                                self.var_lasttouch = (util.sprites.stage.var_FRAME + 5)
                    if (lt(util.sprites.stage.var_PLAYERSY, -16) and lt(self.var_hvy, -0.5)):
                        await self.my_HammerImpact(util, )
                    util.sprites.stage.var_HAMMERX = self.var_tx
                    util.sprites.stage.var_HAMMERY = self.var_ty
                else:
                    if lt(self.var_hvy, -5):
                        self.var_ax = 1
                        util.sprites.stage.var_PLAYERSX += div(0.5, self.var_distance)
                        self.var_distance += -1
            else:
                if lt(self.var_hvy, -5):
                    self.var_ax = -1
                    util.sprites.stage.var_PLAYERSX += div(-0.5, self.var_distance)
                    self.var_distance += -1
        self.var_tx = util.sprites.stage.var_PLAYERX
        self.var_ty = util.sprites.stage.var_PLAYERY
        util.sprites.stage.var_PLAYERX += (self.var_dx + self.var_ax)
        util.sprites.stage.var_PLAYERY += self.var_dy
        await self.my_touchtouching(util, not False, False)
        if eq(self.var_touch, 0):
            return None
        util.sprites.stage.var_PLAYERX += -1
        await self.my_touchtouching(util, not False, False)
        if eq(self.var_touch, 0):
            util.sprites.stage.var_PLAYERSY += (-0.7 * div(util.sprites.stage.var_PLAYERSY, abs(util.sprites.stage.var_PLAYERSY)))
            if gt(abs(util.sprites.stage.var_PLAYERSY), (0 - util.sprites.stage.var_PLAYERSX)):
                util.sprites.stage.var_PLAYERSX += -0.7
            self.var_distance += -1
            return None
        util.sprites.stage.var_PLAYERX += 2
        await self.my_touchtouching(util, not False, False)
        if eq(self.var_touch, 0):
            util.sprites.stage.var_PLAYERSY += (-0.7 * div(util.sprites.stage.var_PLAYERSY, abs(util.sprites.stage.var_PLAYERSY)))
            if gt(abs(util.sprites.stage.var_PLAYERSY), util.sprites.stage.var_PLAYERSX):
                util.sprites.stage.var_PLAYERSX += 0.7
            self.var_distance += -1
            return None
        util.sprites.stage.var_PLAYERX += -1
        util.sprites.stage.var_PLAYERY = toint(self.var_ty)
        self.var_d2 = sqrt(((tonum(arg_lpsx) * tonum(arg_lpsx)) + (tonum(arg_lpsy) * tonum(arg_lpsy))))
        if (lt(div(arg_lpsy, self.var_d2), -0.7) and lt(arg_lpsy, -4)):
            self.sounds.play(("newclunk" + str(pick_rand(1, 5))))
            util.sprites.stage.var_PLAYERSX = (util.sprites.stage.var_PLAYERSX * 0.7)
            util.sprites.stage.var_PLAYERSY = abs((tonum(arg_lpsy) * 0.2))
            self.var_distance = -1
            return None
        else:
            if gt(sqrt(((tonum(arg_lpsx) * tonum(arg_lpsx)) + (tonum(arg_lpsy) * tonum(arg_lpsy)))), 6):
                self.sounds.play(("newscrape" + str(pick_rand(1, 5))))
        await self.my_touchtouching(util, not False, False)
        self.var_d2 = sqrt(((tonum(arg_lpsx) * tonum(arg_lpsx)) + (tonum(arg_lpsy) * tonum(arg_lpsy))))
        if gt(self.var_touch, 0):
            await self.my_lastcontact(util, )
            util.sprites.stage.var_PLAYERX = self.var_tx
            util.sprites.stage.var_PLAYERSX = 0
            util.sprites.stage.var_PLAYERSY = 0
            self.var_distance = -1
            return None
        else:
            self.var_distance += -0.7
            if lt(self.var_d2, 1):
                util.sprites.stage.var_PLAYERSX = (util.sprites.stage.var_PLAYERSX * 0.5)
                util.sprites.stage.var_PLAYERSY = (util.sprites.stage.var_PLAYERSY * 0.5)
                await self.my_lastcontact(util, )
            else:
                self.var_t = div(abs(util.sprites.stage.var_PLAYERSX), self.var_d2)
                util.sprites.stage.var_PLAYERSX = (util.sprites.stage.var_PLAYERSX * (0.3 + (self.var_t * 0.7)))
                if (lt(div(arg_lpsx, self.var_d2), -0.7) and lt(arg_lpsy, -4)):
                    util.sprites.stage.var_PLAYERSY = abs((util.sprites.stage.var_PLAYERSY * 0.2))
                    util.sprites.stage.var_PLAYERSX = (util.sprites.stage.var_PLAYERSX * 0.5)
                    self.var_distance = 1
                else:
                    util.sprites.stage.var_PLAYERSY = (util.sprites.stage.var_PLAYERSY * 0.5)
                    await self.my_lastcontact(util, )

    @on_pressed('x')
    async def key_x_pressed(self, util):
        util.sprites.stage.list_DEBUG.delete_all()
        if False:
            util.sprites.stage.list_DEBUG.append("bang")
            util.sprites.stage.list_DEBUG.append("static")
            util.sprites.stage.list_DEBUG.append(self.var_t)
            util.sprites.stage.var_PLAYERX += -3
            if lt(util.sprites.stage.var_PLAYERSX, 0):
                await self.my_touchtouching(util, not False, False)
            if gt(self.var_touch, 0):
                util.sprites.stage.var_PLAYERX += 4
                if gt(util.sprites.stage.var_PLAYERSX, 0):
                    await self.my_touchtouching(util, not False, False)
                if gt(self.var_touch, 0):
                    util.sprites.stage.var_PLAYERY = self.var_ty
                    await self.my_touchtouching(util, not False, False)
                    if gt(self.var_touch, 0):
                        util.sprites.stage.var_PLAYERX = self.var_tx
                        util.sprites.stage.var_PLAYERSX = 0
                        util.sprites.stage.var_PLAYERSY = 0
                        self.var_dx = 0
                        self.var_dy = 0
                    else:
                        if False:
                            pass
                        util.sprites.stage.var_PLAYERSX = (util.sprites.stage.var_PLAYERSX * 0.5)
                        util.sprites.stage.var_PLAYERSY = (util.sprites.stage.var_PLAYERSY * 0.5)
                        self.var_distance = toint((self.var_distance * 0.7))

    @on_broadcast('new game')
    async def broadcast_NewGame(self, util):
        while True:
            await self.my_GameLoop(util, )

            await self.yield_()

    @warp
    async def my_Gravity(self, util, ):
        if gt(util.sprites.stage.var_PLAYERY, 16000):
            util.sprites.stage.var_PLAYERSX = (util.sprites.stage.var_PLAYERSX * 0.99)
            if gt(util.sprites.stage.var_PLAYERSY, 4):
                util.sprites.stage.var_PLAYERSY = (util.sprites.stage.var_PLAYERSY * 0.99)
            return None
        if lt(util.sprites.stage.var_PLAYERY, 11990):
            util.sprites.stage.var_PLAYERSY += -1.3
            return None
        self.var_t = 1
        self.var_tx = 99999
        self.var_ty = 0
        for _ in range(toint(div(len(self.list_planet), 2))):
            self.var_dx = (tonum(self.list_planet[toint(self.var_t)]) - util.sprites.stage.var_PLAYERX)
            self.var_dy = (tonum(self.list_planet[toint((self.var_t + 1))]) - util.sprites.stage.var_PLAYERY)
            await self.my_distance(util, self.var_dx, self.var_dy)
            if lt(self.var_distance, self.var_tx):
                self.var_tx = self.var_distance
                self.var_ty = self.var_t
            self.var_t += 2
        self.var_dx = (tonum(self.list_planet[toint(self.var_ty)]) - util.sprites.stage.var_PLAYERX)
        self.var_dy = (tonum(self.list_planet[toint((self.var_ty + 1))]) - util.sprites.stage.var_PLAYERY)
        self.var_distance = div((self.var_tx * self.var_tx), 12)
        util.sprites.stage.var_PLAYERSX += div(self.var_dx, self.var_distance)
        util.sprites.stage.var_PLAYERSY += div(self.var_dy, self.var_distance)
        await self.my_distance(util, util.sprites.stage.var_PLAYERSX, util.sprites.stage.var_PLAYERSY)
        if gt(self.var_distance, 15):
            self.var_distance = div(self.var_distance, 15)
            util.sprites.stage.var_PLAYERSX += ((div(util.sprites.stage.var_PLAYERSX, self.var_distance) - util.sprites.stage.var_PLAYERSX) * 0.3)
            util.sprites.stage.var_PLAYERSY += ((div(util.sprites.stage.var_PLAYERSY, self.var_distance) - util.sprites.stage.var_PLAYERSY) * 0.3)
        util.sprites.stage.var_PLAYERSX = (util.sprites.stage.var_PLAYERSX * 0.99)
        if lt(util.sprites.stage.var_PLAYERY, 15000):
            util.sprites.stage.var_PLAYERSY = (util.sprites.stage.var_PLAYERSY * 0.99)

    @on_pressed('g')
    async def key_g_pressed(self, util):
        if False:
            self.list_planet.append((util.sprites.stage.var_CAMERAX + util.inputs.mouse_x))
            self.list_planet.append((util.sprites.stage.var_CAMERAY + util.inputs.mouse_y))

    async def my_GameLoop(self, util, ):
        if eq(util.sprites.stage.var_SFX, "true"):
            self.sounds.set_effect('pitch', 50)
            self.sounds.set_volume(50)
        else:
            self.sounds.set_volume(0)
        self.costume.size = 100
        self.shown = True
        util.sprites.stage.var_BRIGHT = -999
        util.sprites.stage.var_FRAME = 0
        util.sprites.stage.var_MAXLEN = 102
        util.sprites.stage.var_MINLEN = 26
        util.sprites.stage.var_PLAYERX = 0
        util.sprites.stage.var_PLAYERY = 100
        self.var_ContactY = util.sprites.stage.var_PLAYERY
        util.sprites.stage.var_HAMMERX = util.sprites.stage.var_PLAYERX
        util.sprites.stage.var_HAMMERY = util.sprites.stage.var_PLAYERY
        util.sprites.stage.var_PLAYERSX = 0
        util.sprites.stage.var_PLAYERSY = 0
        self.varcamerax = util.sprites.stage.var_PLAYERX
        self.varcameray = util.sprites.stage.var_PLAYERY
        util.sprites.stage.var_CAMERAX = util.sprites.stage.var_PLAYERX
        util.sprites.stage.var_CAMERAY = util.sprites.stage.var_PLAYERY
        util.sprites.stage.var_HAMMERAIR = 100
        self.var_cox = 0
        self.var_coy = 20
        self.var_lasttouch = 0
        util.sprites.stage.list_TIME.delete_all()
        util.send_broadcast("Show")
        util.send_broadcast("Position Level")
        while not (gt(util.sprites.stage.var_PLAYERY, 16000) or lt(util.sprites.stage.var_PLAYERY, -180)):
            util.sprites.stage.var_FRAME += 1
            await self.my_Timer(util, )
            await self.my_AllBroadcastTicks(util, )
            if util.inputs["p"]:
                while not not util.inputs["p"]:
                    await self.yield_()
                while not util.inputs["p"]:
                    await self.sleep(0)

                    await self.yield_()
                while not not util.inputs["p"]:
                    await self.yield_()
            if (util.inputs["q"] and util.inputs["r"]):
                util.send_broadcast("white out")
                for _ in range(10):
                    util.sprites.stage.var_PLAYERSX = 0
                    util.sprites.stage.var_PLAYERSY = -1
                    await self.my_AllBroadcastTicks(util, )

                    await self.yield_()
                return None

            await self.yield_()
        if lt(util.sprites.stage.var_PLAYERY, -180):
            self.shown = False
            util.send_broadcast("out of bounds")
            while not lt(util.sprites.stage.var_CAMERAY, 10):
                util.sprites.stage.var_PLAYERSX = 0
                util.sprites.stage.var_PLAYERSY = -1
                await self.my_AllBroadcastTicks(util, )

                await self.yield_()
            for _ in range(20):
                util.sprites.stage.var_PLAYERSX = 0
                util.sprites.stage.var_PLAYERSY = -1
                await self.my_AllBroadcastTicks(util, )

                await self.yield_()
            util.send_broadcast("white out")
            util.send_broadcast("head")
            for _ in range(10):
                util.sprites.stage.var_PLAYERSX = 0
                util.sprites.stage.var_PLAYERSY = -1
                await self.my_AllBroadcastTicks(util, )

                await self.yield_()
            return None
        util.send_broadcast("SAVE TIME TO CLOUD")
        while True:
            await self.my_AllBroadcastTicks(util, )

            await self.yield_()

    async def my_AllBroadcastTicks(self, util, ):
        util.send_broadcast("centre")
        util.send_broadcast("Fix Collisions")
        util.send_broadcast("Swing Hammer")
        util.send_broadcast("Tick Player")
        util.send_broadcast("Position Level")
        util.send_broadcast("Position Limbs")

    @on_broadcast('centre')
    async def broadcast_centre(self, util):
        util.sprites.stage.var_CAMERAX = toint(util.sprites.stage.var_PLAYERX)
        util.sprites.stage.var_CAMERAY = toint(util.sprites.stage.var_PLAYERY)

    @warp
    async def my_HammerImpact(self, util, ):
        util.sprites.stage.var_HAMMERX += 2
        if gt(util.sprites.stage.var_PLAYERSX, -2):
            await self.my_touchtouching(util, False, not False)
            if eq(self.var_touch, 0):
                util.sprites.stage.var_DEBUG = str(tonum(util.sprites.stage.var_DEBUG) + 1)
                if lt(self.var_hvy, -8):
                    util.sprites.stage.var_PLAYERSX += (-8 * -0.3)
                else:
                    util.sprites.stage.var_PLAYERSX += (self.var_hvy * -0.3)
                util.sprites.stage.var_PLAYERSY = (0.3 * div(util.sprites.stage.var_PLAYERSY, abs(util.sprites.stage.var_PLAYERSY)))
                self.var_distance = -1
                if gt(util.sprites.stage.var_FRAME, self.var_lasttouch):
                    self.sounds.play(("scrape_plastic_" + str(pick_rand(1, 4))))
                    self.var_lasttouch = (util.sprites.stage.var_FRAME + 5)
                return None
        util.sprites.stage.var_HAMMERX += -6
        if lt(util.sprites.stage.var_PLAYERSX, 2):
            await self.my_touchtouching(util, False, not False)
            if eq(self.var_touch, 0):
                util.sprites.stage.var_DEBUG = str(tonum(util.sprites.stage.var_DEBUG) + 1)
                if lt(self.var_hvy, -8):
                    util.sprites.stage.var_PLAYERSX += (-8 * 0.3)
                else:
                    util.sprites.stage.var_PLAYERSX += (self.var_hvy * 0.3)
                util.sprites.stage.var_PLAYERSY = (0.3 * div(util.sprites.stage.var_PLAYERSY, abs(util.sprites.stage.var_PLAYERSY)))
                self.var_distance = -1
                if gt(util.sprites.stage.var_FRAME, self.var_lasttouch):
                    self.sounds.play(("scrape_plastic_" + str(pick_rand(1, 4))))
                    self.var_lasttouch = (util.sprites.stage.var_FRAME + 5)
                return None

    @warp
    async def my_Timer(self, util, ):
        util.sprites.stage.list_TIME.delete_all()
        self.var_t = math.floor(div(util.sprites.stage.var_FRAME, 30))
        if gt(self.var_t, 35999):
            self.var_t = 35999
        self.var_tx = (self.var_t % 60)
        self.var_t = math.floor(div(self.var_t, 60))
        if lt(self.var_tx, 10):
            util.sprites.stage.list_TIME.append(letter_of(str(self.var_tx), 1))
            util.sprites.stage.list_TIME.append(0)
        else:
            util.sprites.stage.list_TIME.append(letter_of(str(self.var_tx), 2))
            util.sprites.stage.list_TIME.append(letter_of(str(self.var_tx), 1))
        self.var_tx = (self.var_t % 60)
        self.var_t = math.floor(div(self.var_t, 60))
        if lt(self.var_tx, 10):
            util.sprites.stage.list_TIME.append(letter_of(str(self.var_tx), 1))
            if gt(self.var_t, 0):
                util.sprites.stage.list_TIME.append(0)
        else:
            util.sprites.stage.list_TIME.append(letter_of(str(self.var_tx), 2))
            util.sprites.stage.list_TIME.append(letter_of(str(self.var_tx), 1))
        self.var_tx = (self.var_t % 60)
        if gt(self.var_t, 0):
            util.sprites.stage.list_TIME.append(letter_of(str(self.var_tx), 1))

    @warp
    async def my_lastcontact(self, util, ):
        if lt(util.sprites.stage.var_PLAYERY, (self.var_ContactY - 650)):
            if eq(util.sprites["Narrator"].var_talking, 0):
                util.send_broadcast("Fall")
        self.var_ContactY = util.sprites.stage.var_PLAYERY

    @on_broadcast('load high score')
    async def broadcast_loadhighscore(self, util):
        util.sprites.stage.var_FRAME = util.sprites.stage.var_FASTEST
        await self.my_Timer(util, )


@sprite('limbs')
class Spritelimbs(Target):
    """Sprite limbs"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -8
        self._ypos = -24
        self._direction = -38.398778025903454
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           14, 100, "all around", [
            {
                'name': "l1",
                'path': "f017bbef3879c18b7ad4e0c7dd149c3b.svg",
                'center': (0, 3),
                'scale': 1
            },
            {
                'name': "l2",
                'path': "d7c759e799998917b713ba154af939ff.svg",
                'center': (0, 3),
                'scale': 1
            },
            {
                'name': "l3",
                'path': "7c91e0c465cda82bac9fdfae681557c5.svg",
                'center': (2, 3),
                'scale': 1
            },
            {
                'name': "l4",
                'path': "c78c1f29700c7e2641e01557477d2918.svg",
                'center': (2, 3),
                'scale': 1
            },
            {
                'name': "l5",
                'path': "66a90fbc2ddd16f3c0cf1f6d0e603403.svg",
                'center': (2, 3),
                'scale': 1
            },
            {
                'name': "l6",
                'path': "dab38c901559bf2cfb2d0e0a3025c3cb.svg",
                'center': (2, 2),
                'scale': 1
            },
            {
                'name': "l7",
                'path': "68f496f991f681679ef76a8b3181f5e1.svg",
                'center': (2, 2),
                'scale': 1
            },
            {
                'name': "l8",
                'path': "25c2a2e844107117d83dde5177f74b04.svg",
                'center': (3, 3),
                'scale': 1
            },
            {
                'name': "l9",
                'path': "659f472ea7e93bce1649a96c54f319a4.svg",
                'center': (5, 3),
                'scale': 1
            },
            {
                'name': "l10",
                'path': "6c42cd0c930e5759842757a1623e24dc.svg",
                'center': (8, 3),
                'scale': 1
            },
            {
                'name': "l11",
                'path': "9359b9506759ef382a78efc72b386b5c.svg",
                'center': (12, 3),
                'scale': 1
            },
            {
                'name': "r1",
                'path': "96a477177721583312f6f4a240f81d3a.svg",
                'center': (0, 4),
                'scale': 1
            },
            {
                'name': "r2",
                'path': "e656871b3377143c7b30e8d93a2574af.svg",
                'center': (0, 5),
                'scale': 1
            },
            {
                'name': "r3",
                'path': "168bc8a3393f926dc9fe6620c9cddd31.svg",
                'center': (2, 6),
                'scale': 1
            },
            {
                'name': "r4",
                'path': "1cb4c5a026973a26eb01a330f8a17da0.svg",
                'center': (2, 7),
                'scale': 1
            },
            {
                'name': "r5",
                'path': "187bd7dc487dca5269c5bd755965ecff.svg",
                'center': (2, 10),
                'scale': 1
            },
            {
                'name': "r6",
                'path': "2ecbad61632050b711c2a391d07c2adc.svg",
                'center': (2, 10),
                'scale': 1
            },
            {
                'name': "r7",
                'path': "a045bec9a546ceb227b28b59a9c3011f.svg",
                'center': (2, 10),
                'scale': 1
            },
            {
                'name': "r8",
                'path': "a28758fa74c79ddab8863c3b35c28774.svg",
                'center': (3, 9),
                'scale': 1
            },
            {
                'name': "r9",
                'path': "1618b89570cfa6014b4df03f51594081.svg",
                'center': (5, 9),
                'scale': 1
            },
            {
                'name': "r10",
                'path': "c0160cc388987c1458c773755f24ec18.svg",
                'center': (8, 9),
                'scale': 1
            },
            {
                'name': "r11",
                'path': "8d8f2ee5f0bacf1a7156d16d74702043.svg",
                'center': (12, 8),
                'scale': 1
            },
            {
                'name': "big",
                'path': "9f1739957bbf542a992dc3326e4db5e0.svg",
                'center': (59, 57),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_type = 1
        self.var_cx = 0
        self.var_cy = 0
        self.var_r = 0
        self.var_r2 = 0
        self.var_r4 = 0
        self.var_a = 15
        self.var_r1r2 = 0
        self.var_c = 0
        self.var_flip = "False"
        self.var_distance = 0
        self.var_touch = 0
        self.var_tx = 0
        self.var_ty = 0
        self.var_ox = 0
        self.var_oy = 0
        self.var_t = 0
        self.var_dx = 0
        self.var_dy = 0
        self.var_lasttx = 0
        self.var_lastty = 0
        self.var_lastmousex = 0
        self.var_lastmousey = 0
        self.var_touchx = 0
        self.var_touchy = 0
        self.varcamerax = 0
        self.varcameray = 0
        self.var_d2 = 0
        self.var_sensePX = 0
        self.var_sensePY = 0
        self.var_sensePV = 0
        self.var_sameHX = 0
        self.var_sameHY = 0
        self.var_sameHV = 0
        self.var_lastEffort = 0
        self.var_effort = 0

        self.list_fix = StaticList(
            []
        )
        self.list_planet = StaticList(
            []
        )

        self.sprite.layer = 10

    @on_broadcast('position level')
    async def broadcast_PositionLevel(self, util):
        self.costume.switch("big")
        self.gotoxy((tonum(util.sprites.stage.list_Hands[toint(self.var_type)]) - tonum(util.sprites.stage.list_Hands[toint((self.var_type + 2))])), (tonum(util.sprites.stage.list_HandsY[toint(self.var_type)]) - tonum(util.sprites.stage.list_HandsY[toint((self.var_type + 2))])))
        self.point_towards(util, "Blank")
        self.var_flip = str(gt(self.ypos, 0))
        self.var_a = self.distance_to(util, "Blank")
        self.gotoxy(tonum(util.sprites.stage.list_Hands[toint(self.var_type)]), tonum(util.sprites.stage.list_HandsY[toint(self.var_type)]))
        self.var_a = (11 - math.floor(div(self.var_a, 4)))
        if lt(self.var_a, 1):
            self.var_a = 1
        if eq(gt(self.var_type, 3), self.var_flip):
            self.var_a += 11
        self.costume.switch(self.var_a)

    @on_broadcast('new game')
    async def broadcast_NewGame(self, util):
        self.var_type = 4
        await self.sleep(0.1)
        self.front_layer(util)
        self.change_layer(util, -1)
        self.shown = True
        self.create_clone_of(util, "_myself_")
        self.var_type = 1

    @on_broadcast('out of bounds')
    async def broadcast_outofbounds(self, util):
        self.shown = False

    @on_broadcast('show')
    async def broadcast_Show(self, util):
        self.shown = True


@sprite('Hammer')
class SpriteHammer(Target):
    """Sprite Hammer"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -77
        self._ypos = 42
        self._direction = -49.83041995828995
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "Hammer Full",
                'path': "33119a6a4f566772371d81217ca7d68e.svg",
                'center': (72, 9),
                'scale': 1
            },
            {
                'name': "Hammer Full2",
                'path': "cf8f897573d08d7c9225f1722f53e4d0.svg",
                'center': (72, 8),
                'scale': 1
            },
            {
                'name': "hitbox",
                'path': "cac23630c5a54a1bda7e87bcb327742a.png",
                'center': (8, 8),
                'scale': 2
            },
            {
                'name': "big",
                'path': "7d549b1af6f36f450876340b67fcb573.svg",
                'center': (198, 140),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_x = 8
        self.var_y = -24
        self.var_distance = 58265.00004747217
        self.var_sx = 0.9995851470840434
        self.var_sy = "-0.02880162719311697"
        self.var_count = 0
        self.var_cx = -14.361991533512601
        self.var_cy = 185.0974005650802
        self.var_r2 = 34467.31449675844
        self.var_r = 185.65374894345237
        self.var_r4 = -11.3669400080177
        self.var_r1r2 = -1.1237889303924857
        self.var_a = "-0.12743705236877498"
        self.var_c = "0.13510786753116838"
        self.var_len = 12



        self.sprite.layer = 11

    @on_broadcast('position level')
    async def broadcast_PositionLevel(self, util):
        self.costume.switch("big")
        await self.my_position(util, )
        self.point_towards(util, "Player")
        self.direction += 180
        self.move(-66)
        self.var_len = div(self.distance_to(util, "Player"), 2)
        if gt(self.var_len, 12):
            self.var_len = 12
        util.sprites.stage.list_Hands.delete_all()
        util.sprites.stage.list_HandsY.delete_all()
        self.var_x = ((util.sprites.stage.var_PLAYERX - 8) - util.sprites.stage.var_CAMERAX)
        self.var_y = ((util.sprites.stage.var_PLAYERY - 1) - util.sprites.stage.var_CAMERAY)
        util.sprites.stage.list_Hands.append(self.var_x)
        util.sprites.stage.list_HandsY.append(self.var_y)
        if False:
            await self.my_intersect(util, self.var_x, self.var_y, self.var_len, self.xpos, self.ypos, 20, not False)
        util.sprites.stage.list_Hands.append(self.var_cx)
        util.sprites.stage.list_HandsY.append(self.var_cy)
        util.sprites.stage.list_Hands.append(self.xpos)
        util.sprites.stage.list_HandsY.append(self.ypos)
        self.move(8)
        self.var_x = ((util.sprites.stage.var_PLAYERX + 8) - util.sprites.stage.var_CAMERAX)
        self.var_y = ((util.sprites.stage.var_PLAYERY - 1) - util.sprites.stage.var_CAMERAY)
        util.sprites.stage.list_Hands.append(self.var_x)
        util.sprites.stage.list_HandsY.append(self.var_y)
        if False:
            await self.my_intersect(util, self.var_x, self.var_y, self.var_len, self.xpos, self.ypos, 20, False)
        util.sprites.stage.list_Hands.append(self.var_cx)
        util.sprites.stage.list_HandsY.append(self.var_cy)
        util.sprites.stage.list_Hands.append(self.xpos)
        util.sprites.stage.list_HandsY.append(self.ypos)
        self.move((66 - 8))
        self.costume.switch("Hammer Full")

    @warp
    async def my_distance(self, util, arg_dx, arg_dy):
        self.var_distance = sqrt(((tonum(arg_dx) * tonum(arg_dx)) + (tonum(arg_dy) * tonum(arg_dy))))

    @warp
    async def my_position(self, util, ):
        self.gotoxy(toint((util.sprites.stage.var_HAMMERX - util.sprites.stage.var_CAMERAX)), toint((util.sprites.stage.var_HAMMERY - util.sprites.stage.var_CAMERAY)))

    @warp
    async def my_intersect(self, util, arg_x1, arg_y1, arg_r1, arg_x2, arg_y2, arg_r2, arg_left):
        self.var_cx = (arg_x1 - arg_x2)
        self.var_cy = (arg_y1 - arg_y2)
        self.var_r2 = ((self.var_cx * self.var_cx) + (self.var_cy * self.var_cy))
        self.var_r = sqrt(self.var_r2)
        if (gt(abs((arg_r1 - arg_r2)), self.var_r) or lt((arg_r1 + arg_r2), self.var_r)):
            return None
        self.var_r4 = (self.var_r2 * self.var_r2)
        self.var_r1r2 = ((arg_r1 * arg_r1) - (arg_r2 * arg_r2))
        self.var_a = str(div(self.var_r1r2, (2 * self.var_r2)))
        self.var_c = str(sqrt(((div((2 * ((arg_r1 * arg_r1) + (arg_r2 * arg_r2))), self.var_r2) - div((self.var_r1r2 * self.var_r1r2), self.var_r4)) - 1)))
        self.var_r = (div((arg_x1 + arg_x2), 2) + (tonum(self.var_a) * (arg_x2 - arg_x1)))
        self.var_r2 = div((tonum(self.var_c) * (arg_y2 - arg_y1)), 2)
        self.var_r4 = (div((arg_y1 + arg_y2), 2) + (tonum(self.var_a) * (arg_y2 - arg_y1)))
        self.var_r1r2 = div((tonum(self.var_c) * (arg_x1 - arg_x2)), 2)
        if eq(arg_left, lt(self.var_r2, 0)):
            self.var_cx = (self.var_r + self.var_r2)
            self.var_cy = (self.var_r4 + self.var_r1r2)
        else:
            self.var_cx = (self.var_r - self.var_r2)
            self.var_cy = (self.var_r4 - self.var_r1r2)

    @on_broadcast('new game')
    async def broadcast_NewGame(self, util):
        self.front_layer(util)
        self.change_layer(util, -1)
        self.costume.switch("Hammer Full")
        self.costume.rotation_style = 'all around'
        self.shown = True
        await self.sleep(0.2)
        self.front_layer(util)
        self.change_layer(util, -1)

    @on_broadcast('out of bounds')
    async def broadcast_outofbounds(self, util):
        self.shown = False

    @on_broadcast('show')
    async def broadcast_Show(self, util):
        self.shown = True


@sprite('Head')
class SpriteHead(Target):
    """Sprite Head"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = -19
        self._direction = -69.689186641815
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           3, 100, "all around", [
            {
                'name': "right",
                'path': "50be8ee3a861ef5d112e06909c3544ad.svg",
                'center': (25, 33),
                'scale': 1
            },
            {
                'name': "right2",
                'path': "be3f83bcba6702e70803d175b91ee5cc.svg",
                'center': (25, 33),
                'scale': 1
            },
            {
                'name': "right3",
                'path': "425c0985ab1cc229adfa76506f37d84f.svg",
                'center': (25, 33),
                'scale': 1
            },
            {
                'name': "left",
                'path': "7c1d421f4270c6f4cbf5e385231a3e32.svg",
                'center': (25, 1),
                'scale': 1
            },
            {
                'name': "left2",
                'path': "d33cfb80b32364cd41102285f8ed61ac.svg",
                'center': (25, 1),
                'scale': 1
            },
            {
                'name': "right4",
                'path': "d64e73be3dcc8609fa4d37122363a1ee.svg",
                'center': (25, 1),
                'scale': 1
            },
            {
                'name': "big",
                'path': "9d0c46a08c82236f46c68bf92ce70c04.svg",
                'center': (113, 88),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_blinktime = 19.01824879544167
        self.var_head = 3
        self.var_distance = 0
        self.var_touch = 0
        self.var_tx = 0
        self.var_ty = 0
        self.var_ox = 0
        self.var_oy = 0
        self.var_t = 0
        self.var_dx = 0
        self.var_dy = 0
        self.var_lasttx = 0
        self.var_lastty = 0
        self.var_lastmousex = 0
        self.var_lastmousey = 0
        self.var_touchx = 0
        self.var_touchy = 0
        self.varcamerax = 0
        self.varcameray = 0
        self.var_d2 = 0
        self.var_sensePX = 0
        self.var_sensePY = 0
        self.var_sensePV = 0
        self.var_sameHX = 0
        self.var_sameHY = 0
        self.var_sameHV = 0
        self.var_lastEffort = 0
        self.var_effort = 0

        self.list_fix = StaticList(
            []
        )
        self.list_planet = StaticList(
            []
        )

        self.sprite.layer = 4

    @on_broadcast('position level')
    async def broadcast_PositionLevel(self, util):
        self.costume.switch("big")
        self.goto(util, "Player")
        self.ypos += 4
        self.point_towards(util, "_mouse_")
        self.direction = (((abs(self.direction) - 90) * 0.5) + 90)
        if lt(util.inputs.mouse_x, 0):
            self.direction = (0 - self.direction)
            self.costume.switch("left")
        else:
            self.costume.switch("right")
        if gt(util.timer(), self.var_blinktime):
            self.costume.switch((self.costume.number + 2))
            if gt(util.timer(), (self.var_blinktime + 0.03)):
                await self.my_SetBlink(util, )
        else:
            if lt(abs(util.inputs.mouse_x), 64):
                self.costume.next()

    @on_broadcast('out of bounds')
    async def broadcast_outofbounds(self, util):
        self.shown = False

    @on_broadcast('new game')
    async def broadcast_NewGame(self, util):
        self.shown = True
        await self.my_SetBlink(util, )

    @on_broadcast('show')
    async def broadcast_Show(self, util):
        self.shown = True

    @warp
    async def my_SetBlink(self, util, ):
        self.var_blinktime = (util.timer() + pick_rand(0.8, 7))

    @on_broadcast('head')
    async def broadcast_head(self, util):
        if gt(self.var_head, 0):
            self.var_head += -1
        else:
            self.costume.size = (1.2 * round(self.costume.size))

    @on_green_flag
    async def green_flag(self, util):
        self.var_head = 3
        self.costume.size = 100


@sprite('Level')
class SpriteLevel(Target):
    """Sprite Level"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 300
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           149, 100, "all around", [
            {
                'name': "blank",
                'path': "cd21514d0531fdffb22204e0ec5ed84a.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "9x27x",
                'path': "287f7441556f832093cbdf88f1dd2887.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "9x28x",
                'path': "907036b2c6abb3dc0eb7249713693972.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "10x28x",
                'path': "5e1c692ea67c74fde139730dea1ea2bd.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "10x29x",
                'path': "eda6be1f49e20c4efc4269c9bb84afff.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "8x13x",
                'path': "c354eefec304c7f5d524588f6cb6659e.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "7x13x",
                'path': "9ea764620d92bf387f00b1427e80a32e.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "-1x2x",
                'path': "6a98afb494331c10bc785230c1220175.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "0x2x",
                'path': "6a98afb494331c10bc785230c1220175.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "10x43x",
                'path': "7957bcdb1ff4d637fef7b3683f049be9.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "8x43x",
                'path': "699421b94ce3903586caf1a3b3996f92.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "11x40x",
                'path': "0d113367e5d21a36d11b75874b07b0bb.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "9x41x",
                'path': "6e9a3e321cc45be0730c1f019a815941.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "8x39x",
                'path': "25301ce206dd3bb9d383a233fa16d421.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "4x33x",
                'path': "9be6427a76381ccbe3896bc2b907fabe.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "4x32x",
                'path': "190d9458a3afa3ff1d48679f5ef196c4.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "3x33x",
                'path': "036f58d2c1c8502eb4be82bb5e044cbb.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "3x32x",
                'path': "99961da9cf6228b0c48d3b0941a00c9a.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "3x31x",
                'path': "8d542cda79284adc20cc74538a36d453.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "3x30x",
                'path': "746c1162efb6e10220025099ae1afa73.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "3x29x",
                'path': "96b8f562d6759a3f1940c669cf8f8cfb.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "4x31x",
                'path': "f41570c5fbc911057bcda6572bbcb94b.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "4x30x",
                'path': "3d3bf704b4b8ee803820ba3e2f4b795f.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "4x29x",
                'path': "5361b715c036265113429786cc37ccb5.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "4x28x",
                'path': "3e2690ea63a8b8cb2c0849b1825ae178.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "4x27x",
                'path': "cc689327330942bc84e7271328c266c3.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "4x26x",
                'path': "9e778a087602fbde55a7beb005b3317c.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "12x35x",
                'path': "290f0bdf8de78517a81241d06becf7b4.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "12x34x",
                'path': "ca931ba3795999ee33b478efc7051b56.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "12x33x",
                'path': "3a89e6d08a04993431bdfbaf74d327e6.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "9x29x",
                'path': "db05b8d3d6e719d0cfb82e628bb00ba5.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "11x35x",
                'path': "b10ef48d3b03facf05364dd8111c25c5.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "11x32x",
                'path': "302c1290adf10f3da934289c92492328.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "11x34x",
                'path': "1a216fe26aa0a9f2b75986440eeef60f.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "11x33x",
                'path': "40c4361fe1f85220fde5bb73921bc427.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "11x31x",
                'path': "a9573df16e9782cb1146dfc3b68b2412.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "11x28x",
                'path': "f378a9a3ee9442ea167e1b83c4b69f46.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "11x30x",
                'path': "c33f5db71f1534a09136142c8ca6858f.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "7x42x",
                'path': "4fd78ca6658209ee12b91c7876355a6b.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "11x29x",
                'path': "b9ffc762005cc8dce296ce3d56bcb290.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "10x37x",
                'path': "198a9cc9b89229c7b633b6bc105c439e.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "9x37x",
                'path': "f616683ac296dc668869a4528b3f197a.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "9x36x",
                'path': "6a98afb494331c10bc785230c1220175.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "9x35x",
                'path': "3743c4da09263711c770c08795e0f2e1.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "9x34x",
                'path': "bf54d414e26ab353c3c1b29a39b4c04a.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "9x33x",
                'path': "f2a1beaff9b43d3c7731fc0a56cf8bb7.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "9x30x",
                'path': "f932e9dc2684149eb877502fae44d238.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "9x32x",
                'path': "8bfe3e6d9d20aea3e9917cfbe8cc2a4a.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "8x32x",
                'path': "4087e6115514069288fb23d999303b1c.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "9x31x",
                'path': "762ae69b77b88f1bd72d7048ac081b38.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "8x31x",
                'path': "566f63ca033536fe025816b4a959edb9.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "8x30x",
                'path': "9f10f15032122d551bb3ead0c2152534.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "7x30x",
                'path': "ff21cc626652ce8633203a4fda7bb61f.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "8x29x",
                'path': "12fbb6194138d31d8ebe61c0ff787122.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "7x29x",
                'path': "60e9480158aaf10e87c7bf38069db344.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "7x28x",
                'path': "223047a53710a87cca168efd7b15681e.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "6x28x",
                'path': "c77a885a5749137b6502cf80e411d2bb.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "6x27x",
                'path': "b15ed0d0c79dcf420d12c1da20ad0853.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "5x27x",
                'path': "3151c1b238765f702cfe0d5a3985fe9d.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "6x26x",
                'path': "850508db6475641d4f9f67922b993893.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "5x26x",
                'path': "b96674567fe7d001261636e73dfaf63e.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "6x25x",
                'path': "9e189ec170f9f8819522aa8fa157562d.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "5x25x",
                'path': "faaf404ac58d98b1c42aa09d42d3f604.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "6x6x",
                'path': "41544fad1ecd5fe0970b8e11474e4576.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "10x27x",
                'path': "cb2a67b11569459e04e8cefbae1116a7.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "11x27x",
                'path': "fa6748870cceddab8124bcdbf13146c7.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "9x25x",
                'path': "801553effb16308c6f61389c9e4c7cf3.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "8x25x",
                'path': "8272b98a9f134ec33c3873ca747505ef.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "7x25x",
                'path': "63fe35fd28445d2f5d42a16558437b93.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "10x26x",
                'path': "906a550cdbcfdfa412b40e1eca9e0c57.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "9x26x",
                'path': "f70cdd7f5800b3d040dff5a90998d263.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "11x24x",
                'path': "6eb49ff8c379f296f40abbeb80e66bd3.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "11x26x",
                'path': "75d554c711c95f413d1f11ee41947807.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "11x25x",
                'path': "8673450c3adc0220f3763578e59f6c87.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "10x23x",
                'path': "f8231317c734973d929d28bac68a8b63.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "10x25x",
                'path': "706a4cd462ac8768db6f26af00b80c60.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "10x24x",
                'path': "a417f8b3ea9956d1c8203a272a026c89.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "9x22x",
                'path': "f5da665476e8ce7f03b91ee2f4391ea7.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "9x24x",
                'path': "942b53921a3028d2f46778321a6a1356.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "9x23x",
                'path': "3711912594fc074086e98fd338a292ca.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "7x20x",
                'path': "8eb2b0b3a87933e5ab46e18a97cf04c0.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "8x23x",
                'path': "ef76127edb352eb02075f3c23e2128bf.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "8x22x",
                'path': "23e2b1fdd2f63c8221787f45f562160c.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "8x21x",
                'path': "ba318bf34b1bc1a38c629eea83cbce59.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "7x22x",
                'path': "dc73e003f40627e4b63daacc00fe5f62.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "7x21x",
                'path': "f8a56c7528f8a9bbc7895ecccc1ea5b0.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "6x21x",
                'path': "43a16971a5ee1262593e2ede32ed47e3.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "6x20x",
                'path': "5ea23a79bd01fe629c94d56289f23428.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "6x19x",
                'path': "d68a1f9acd893b7a3e88c86edc33f4bb.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "6x18x",
                'path': "7622596f6398f2de10285418ec15af50.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "5x20x",
                'path': "1ae25d80538dacb0aded33d7517fb1e2.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "5x19x",
                'path': "7bf4fa8eba40faf44b553df0b16956a6.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "5x18x",
                'path': "b83998e11713ed2988419eb8528b1fb5.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "4x17x",
                'path': "c4fc2c0122757cb04d0d2efefeab168c.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "4x15x",
                'path': "eaaa9b6c09d2b66c2e7f80a39dfdff8b.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "4x16x",
                'path': "9546ef9f7a44536426fb78382c7f5cf3.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "-1x0x",
                'path': "fc713fa3ea5e13f7212d6830bb6cb6fc.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "-1x1x",
                'path': "6a98afb494331c10bc785230c1220175.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "7x9x",
                'path': "e0de1417077a1d2623d2f08c86dd1e38.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "5x5x",
                'path': "43793cf8d8788490b70252d6c3dc4835.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "3x14x",
                'path': "208f4b07daea51c402cfaa05e60911db.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "7x17x",
                'path': "f9fce757b14b8812448edc49517b41f9.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "8x12x",
                'path': "738c0bb88c7243396275f94a1030f2a1.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "7x12x",
                'path': "ea8590165cd3b744496d0e190277f2a7.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "5x17x",
                'path': "3ca9d02a11abbf94fe8d7fc932fd187f.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "6x17x",
                'path': "d662a889b6f9fa1623f0399d67a8df87.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "7x16x",
                'path': "50043475a11c909892a68e06464bb358.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "7x15x",
                'path': "0a6c82995f88ebadac68c8dbf2eb8d30.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "6x16x",
                'path': "56f65327b2fc3619b972a14a191d89dd.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "5x16x",
                'path': "c7e06fe2abef58b8555a7215628776a6.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "6x15x",
                'path': "05e246937eeec0211269679597d4e0b8.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "5x15x",
                'path': "69b0d420138a12db7fd46c962652abe0.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "6x14x",
                'path': "420f50439eb1ff9eb3f63758bb1bae60.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "5x14x",
                'path': "49c9e312c4d27d5be20ed57a89be8c3b.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "6x13x",
                'path': "4b4cf11409ffc6c60422dff9136a181b.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "6x12x",
                'path': "f6ad59f35a360de0bb78d7c641bdffca.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "5x13x",
                'path': "3eb3d539a7475e53d62fabd1512df370.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "5x12x",
                'path': "44426d50702739560f7b3c20b5e9bfa0.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "3x13x",
                'path': "7b4a27bc971986d396f13eb472e75be8.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "4x13x",
                'path': "0237ff258e49f04171f68dcfe2cb0efc.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "3x12x",
                'path': "2927b80cc96ca1733e2ddb7a79fe67e8.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "3x11x",
                'path': "329033987ca1c2224631c921506cf2bc.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "4x12x",
                'path': "35c819088ca54fa34818e2d25bf657f7.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "8x11x",
                'path': "8ddc6e88c76bf05df6c571e9b711f6b1.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "4x11x",
                'path': "4aff90c712849ec9c8172cc14dd5d308.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "4x10x",
                'path': "67b196aafba1b371d73b1fc8426972c7.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "5x10x",
                'path': "b54f2f246dc55f1c678c1a99e8bfe767.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "5x11x",
                'path': "0d3ee7594bedd4650534902157c886ab.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "7x11x",
                'path': "ba53bb1ddd325228f1eafee1733b9e29.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "6x11x",
                'path': "843ec9bfd8216e7cfa1918599b3d7622.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "6x10x",
                'path': "adffcbc3e3aa52143884e3fdcba866f0.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "7x10x",
                'path': "f8d9c0bd5ebd2606c155e1ef27638cb9.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "8x10x",
                'path': "ec28b3b45589690226c7207c2aa0ec22.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "8x9x",
                'path': "ea198882f4c1580f1c4938812da6ac20.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "9x7x",
                'path': "e2f84c5d1819f520da83fc9d4a69f522.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "8x7x",
                'path': "14ffe4e1adc2d8f48201841c9b3f7664.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "8x8x",
                'path': "13b14341e7ee420862f356c3578d100c.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "9x8x",
                'path': "3517dd7e77d9bc811c5deb104500fa4c.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "0x0x",
                'path': "31f7e98de57337ed66d668c21224bf1c.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "1x0x",
                'path': "855ce8b408ced2ebbdd2c4f12ce6e77b.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "2x0x",
                'path': "cbf27188324120f70b98eec0f3c3b187.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "3x0x",
                'path': "72ab52ac69538252512cafdf3fa2f38c.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "4x0x",
                'path': "0bea5fe7800a54e668f2845e30bdc321.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "5x0x",
                'path': "6dafb0fb095b96b120478aaaa5614a1d.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "6x2x",
                'path': "126e07f3449aac31626d28268ace6894.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "6x7x",
                'path': "a60c906a7054e8c46d2a4a09d361143b.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "6x8x",
                'path': "0298f8853099a7361017c93c5e589319.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "7x7x",
                'path': "f4c0b2b0efad2d963e4c6c6a7e09bec2.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "7x8x",
                'path': "cba827ac269e22bebf95ee3fcbc6a1e4.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "0x1x",
                'path': "6a98afb494331c10bc785230c1220175.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "2x1x",
                'path': "8b239a7518838247d116c2b135697ec0.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "3x1x",
                'path': "01ca59b9f2848c0c0fbb09326c85653c.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "4x1x",
                'path': "be94b3026ffa69fee3fc1660cba0bf48.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "5x1x",
                'path': "3c560d7894cebc68a117edf2afd443d7.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "5x2x",
                'path': "7ec991aabd5efd2640895af30bf5f794.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "5x6x",
                'path': "1963bfc887d3b5de500364164ae1d06a.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "6x3x",
                'path': "1e5d3513dfba44e6b9234ccb3d242514.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "6x4x",
                'path': "b81b432a7e48b529795fb8d1a81da145.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "6x5x",
                'path': "243f8fd11a73aca8f15a29f2ecd6a95a.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "7x3x",
                'path': "8a660e660bcee2f47fc9752f5eb88fb9.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "7x4x",
                'path': "589bc696f4a37b5b4424117515af0ec1.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "7x5x",
                'path': "6c8616fd930e024e28f1d7715d9a31de.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "7x6x",
                'path': "11fee64093f14f0c2487801b7b3b2636.png",
                'center': (480, 360),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_x = 0
        self.var_y = 0
        self.var_lx = 0
        self.var_ly = 1
        self.var_costume = "0x1x"
        self.var_t = "0x1x"



        self.sprite.layer = 3

    @on_broadcast('position level')
    async def broadcast_PositionLevel(self, util):
        await self.my_positionit(util, )
        self.var_t = (str(self.var_lx) + ("x" + (str(self.var_ly) + "x")))
        if not eq(self.var_costume, self.var_t):
            self.var_costume = self.var_t
            self.costume.switch(self.var_costume)
            if eq(self.var_costume, self.costume.name):
                self.shown = True
            else:
                self.shown = False

    @warp
    async def my_positionA(self, util, arg_x, arg_y):
        if lt(arg_x, -464):
            self.var_lx += 2
            await self.my_positionit(util, )
        else:
            if gt(arg_x, 464):
                self.var_lx += -2
                await self.my_positionit(util, )
            else:
                if lt(arg_y, -344):
                    self.var_ly += 2
                    await self.my_positionit(util, )
                else:
                    if gt(arg_y, 344):
                        self.var_ly += -2
                        await self.my_positionit(util, )
                    else:
                        self.gotoxy(arg_x, arg_y)

    @warp
    async def my_positionit(self, util, ):
        await self.my_positionA(util, ((self.var_lx * 464) - util.sprites.stage.var_CAMERAX), ((self.var_ly * 344) - util.sprites.stage.var_CAMERAY))

    @on_pressed('p')
    async def key_p_pressed(self, util):
        self.var_costume = ""

    @on_broadcast('new game')
    async def broadcast_NewGame(self, util):
        self.costume.size = 100
        self.var_costume = ""
        self.var_lx = 0
        self.var_ly = 0
        self.create_clone_of(util, "_myself_")
        self.var_lx = 1
        self.create_clone_of(util, "_myself_")
        self.var_ly = 1
        self.create_clone_of(util, "_myself_")
        self.var_lx = 0

    @on_broadcast('centre')
    async def broadcast_centre(self, util):
        await self.my_positionit(util, )
        self.var_t = (str(self.var_lx) + ("x" + (str(self.var_ly) + "x")))
        if not eq(self.var_costume, self.var_t):
            self.var_costume = self.var_t
            self.costume.switch(self.var_costume)
            if eq(self.var_costume, self.costume.name):
                self.shown = True
            else:
                self.shown = False


@sprite('Background')
class SpriteBackground(Target):
    """Sprite Background"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 278.6666666666667
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           9, 100, "all around", [
            {
                'name': "costume1",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "z0x0",
                'path': "bb1e86e893f60446efb6c31c3ad445d4.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "z1x0",
                'path': "6041bb9e3d26c532754fd98a4533fc15.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "0x0",
                'path': "12c8ca799302d97be9b711bb430e4b03.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "1x0",
                'path': "e02b8fce3643a04e43ce4ca4a60df6d0.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "-1x0",
                'path': "10db9ab6cca0dd940fce76ed37f8700d.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "2x0",
                'path': "8b3eac90c5b83fe087a48347de1ab53f.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "background",
                'path': "d90fd854dccfbf64464a55cba66fd6e7.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "background2",
                'path': "ea6218f13788c6672aecce16fbdf2d8c.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "background3",
                'path': "1c1c4406b49369a654fedf1c9d555d69.png",
                'center': (478, 310),
                'scale': 2
            },
            {
                'name': "background4",
                'path': "76756e2ca8004e71638194ebf55a39fb.png",
                'center': (478, 310),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_costume = 0
        self.var_lx = 0
        self.var_ly = 1
        self.var_t = "1x0"



        self.sprite.layer = 1

    @warp
    async def my_positionit(self, util, ):
        await self.my_positionA(util, ((self.var_lx * 448) - div(util.sprites.stage.var_CAMERAX, 1.5)), ((self.var_ly * 308) - div(util.sprites.stage.var_CAMERAY, 1.5)))

    @on_broadcast('position level')
    async def broadcast_PositionLevel(self, util):
        await self.my_positionit(util, )

    @warp
    async def my_positionA(self, util, arg_x, arg_y):
        if lt(arg_x, -448):
            self.var_lx += 2
            await self.my_positionit(util, )
        else:
            if gt(arg_x, 448):
                self.var_lx += -2
                await self.my_positionit(util, )
            else:
                if lt(arg_y, -308):
                    self.var_ly += 2
                    await self.my_positionit(util, )
                else:
                    if gt(arg_y, 308):
                        self.var_ly += -2
                        await self.my_positionit(util, )
                    else:
                        self.gotoxy(arg_x, arg_y)

    @on_broadcast('new game')
    async def broadcast_NewGame(self, util):
        self.back_layer(util)
        self.costume.switch("background3")
        self.costume.set_effect('brightness', 0)
        self.gotoxy(0, 0)
        self.var_costume = 0
        self.var_lx = 0
        self.var_ly = 0
        self.create_clone_of(util, "_myself_")
        self.var_lx = 1
        self.create_clone_of(util, "_myself_")
        self.var_ly = 1
        self.create_clone_of(util, "_myself_")
        self.var_lx = 0


@sprite('Comment')
class SpriteComment(Target):
    """Sprite Comment"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 180
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "blank",
                'path': "cd21514d0531fdffb22204e0ec5ed84a.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "1x0",
                'path': "1167c6f8050718a27017d4882bee778e.png",
                'center': (281, 352),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_x = 0
        self.var_y = 0
        self.var_lx = 0
        self.var_ly = 1
        self.var_costume = "0x1"
        self.var_t = "0x1"



        self.sprite.layer = 2

    @on_broadcast('position level')
    async def broadcast_PositionLevel(self, util):
        await self.my_positionit(util, )
        self.var_t = ("" + (str(self.var_lx) + ("x" + str(self.var_ly))))
        if not eq(self.var_costume, self.var_t):
            self.var_costume = self.var_t
            self.costume.switch(self.var_costume)
            if eq(self.var_costume, self.costume.name):
                self.shown = True
                await self.my_positionit(util, )
            else:
                self.shown = False

    @warp
    async def my_positionA(self, util, arg_x, arg_y):
        if lt(arg_x, -464):
            self.var_lx += 2
            await self.my_positionit(util, )
        else:
            if gt(arg_x, 464):
                self.var_lx += -2
                await self.my_positionit(util, )
            else:
                if lt(arg_y, -344):
                    self.var_ly += 2
                    await self.my_positionit(util, )
                else:
                    if gt(arg_y, 344):
                        self.var_ly += -2
                        await self.my_positionit(util, )
                    else:
                        self.gotoxy(arg_x, arg_y)

    @warp
    async def my_positionit(self, util, ):
        await self.my_positionA(util, ((self.var_lx * 464) - div(util.sprites.stage.var_CAMERAX, 1.5)), ((self.var_ly * 344) - div(util.sprites.stage.var_CAMERAY, 1.5)))

    @on_pressed('p')
    async def key_p_pressed(self, util):
        self.var_costume = ""

    @on_broadcast('new game')
    async def broadcast_NewGame(self, util):
        self.costume.size = 100
        self.var_costume = ""
        self.var_lx = 0
        self.var_ly = 0
        self.create_clone_of(util, "_myself_")
        self.var_lx = 1
        self.create_clone_of(util, "_myself_")
        self.var_ly = 1
        self.create_clone_of(util, "_myself_")
        self.var_lx = 0


@sprite('Cursor')
class SpriteCursor(Target):
    """Sprite Cursor"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -232
        self._ypos = 177
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "costume1",
                'path': "6de29caa2b3dcb52f2f934a2a9900c2e.svg",
                'center': (15, 15),
                'scale': 1
            },
            {
                'name': "costume2",
                'path': "03c203cd5c87efcfdf7fc9bd662ae7dc.svg",
                'center': (16, 16),
                'scale': 1
            },
            {
                'name': "big",
                'path': "b151663d1a675bcf77c006e5a355cb13.svg",
                'center': (87, 78),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])





        self.sprite.layer = 13

    @on_broadcast('position level')
    async def broadcast_PositionLevel(self, util):
        self.costume.switch("big")
        self.goto(util, "_mouse_")
        self.xpos += ((util.sprites.stage.var_PLAYERX + tonum(util.sprites["Player"].var_cox)) - util.sprites.stage.var_CAMERAX)
        self.ypos += ((util.sprites.stage.var_PLAYERY + tonum(util.sprites["Player"].var_coy)) - util.sprites.stage.var_CAMERAY)
        self.costume.switch("costume1")

    @on_broadcast('new game')
    async def broadcast_NewGame(self, util):
        self.shown = True
        self.costume.set_effect('ghost', 60)
        await self.sleep(1)
        self.front_layer(util)

    @on_broadcast('win')
    async def broadcast_Win(self, util):
        self.shown = False

    @on_broadcast('win - record')
    async def broadcast_WinRecord(self, util):
        self.shown = False


@sprite('Splash')
class SpriteSplash(Target):
    """Sprite Splash"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           16, 100, "all around", [
            {
                'name': "Background",
                'path': "92c2c98276c5f59a3584fe7e1924f781.svg",
                'center': (240, 208),
                'scale': 1
            },
            {
                'name': "Block",
                'path': "3b9bfa142a42264ef387fe4630220cfa.svg",
                'center': (250, 185),
                'scale': 1
            },
            {
                'name': "Hammer",
                'path': "5cb28344eb75cf26a3076919c14b293f.svg",
                'center': (38, 448),
                'scale': 1
            },
            {
                'name': "highscore",
                'path': "c9ae846f0998e94b43f55c87f2ba0021.svg",
                'center': (241, 183),
                'scale': 1
            },
            {
                'name': "title",
                'path': "2bf1f423cbab1b52140b44fa99024198.svg",
                'center': (9, 67),
                'scale': 1
            },
            {
                'name': "High Score",
                'path': "17bf45da75d78112339b884767ae7559.svg",
                'center': (10, 130),
                'scale': 1
            },
            {
                'name': "New Game",
                'path': "794500e428ebbaf9a49fc8064274854c.svg",
                'center': (8, -19),
                'scale': 1
            },
            {
                'name': "Sound Effects",
                'path': "a923a1883532682c88527711f916a91d.svg",
                'center': (8, -44),
                'scale': 1
            },
            {
                'name': "Sound Effects Mute",
                'path': "2cbb926da4c6cdc15a576d31a5b2379f.svg",
                'center': (9, -44),
                'scale': 1
            },
            {
                'name': "Commentary",
                'path': "a39a58a2d5716c7448dbdaf96840b5f0.svg",
                'center': (8, -44),
                'scale': 1
            },
            {
                'name': "Commentary Mute",
                'path': "e11a5161c7fba7130b2c9baf77653fd8.svg",
                'center': (9, -44),
                'scale': 1
            },
            {
                'name': "white",
                'path': "797b03bdb8cf6ccfc30c0692d533d998.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "black",
                'path': "279daf26b7b43e0d5df0db327dc5ccce.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "stars",
                'path': "831bf5d7e82289758823cec983e1ad7d.svg",
                'center': (240, 420),
                'scale': 1
            },
            {
                'name': "end title",
                'path': "b3b9b329b749a0cf91993fa883a26a25.svg",
                'center': (149, 117),
                'scale': 1
            },
            {
                'name': "world record",
                'path': "37c39509c82cd0a0d036eb47f23c4c8a.svg",
                'center': (176, 118),
                'scale': 1
            },
            {
                'name': "splash",
                'path': "9f07f0e5794276d476b32f0f0c0ed646.png",
                'center': (480, 360),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "menuhit1",
                'path': "64eeecb45494b45b727ec1872f7401df.wav"
            },
            {
                'name': "menurelease",
                'path': "30bacae755d42f8878f7f798876f070b.wav"
            }
        ])

        self.var_menuy = 0
        self.var_sy = 1.5
        self.var_t = 0



        self.sprite.layer = 16

    @on_green_flag
    async def green_flag(self, util):
        self.costume.switch("splash")
        self.gotoxy(0, 0)
        self.direction = 90
        self.front_layer(util)
        self.shown = True
        await self.sleep(2)
        util.sprites.stage.var_SFX = "true"
        util.sprites.stage.var_COMMENTARY = "true"
        self.front_layer(util)
        self.shown = True
        self.costume.switch("Background")
        self.gotoxy(0, 0)
        self.direction = 90
        self.create_clone_of(util, "_myself_")
        self.costume.switch("Block")
        self.gotoxy(0, 0)
        self.create_clone_of(util, "_myself_")
        self.costume.switch("Hammer")
        self.gotoxy(-41, -311)
        self.direction = 180
        self.create_clone_of(util, "_myself_")
        self.shown = False
        self.costume.switch("title")
        self.direction = 90
        self.gotoxy(0, 0)
        self.create_clone_of(util, "_myself_")
        self.costume.switch("Sound Effects")
        self.var_menuy = -81
        self.create_clone_of(util, "_myself_")
        self.costume.switch("Commentary")
        self.var_menuy = -108
        self.create_clone_of(util, "_myself_")
        self.costume.switch("New Game")
        self.var_menuy = -30
        self.create_clone_of(util, "_myself_")
        self.var_menuy = 0
        self.costume.switch("High Score")
        self.costume.set_effect('ghost', 100)

    @on_clone_start
    async def clone_start(self, util):
        if eq(self.costume.name, "Hammer"):
            await self.sleep(0.5)
            for _ in range(8):
                self.direction -= 10

                await self.yield_()
            self.direction -= 10
            self.sounds.set_effect('pitch', 0)
            self.sounds.play("menuhit1")
            util.send_broadcast("splash - hit")
            while True:
                if gt(util.inputs.mouse_x, 160):
                    if gt(util.inputs.mouse_y, 110):
                        self.gotoxy(0, 0)
                        self.costume.switch("highscore")
                        await util.sprites["High Score"].broadcast_showhighscoretable(util)
                        while not (util.inputs.mouse_down and gt(util.inputs.mouse_x, -30)):
                            await self.sleep(0)

                            await self.yield_()
                        await util.sprites["High Score"].broadcast_hidehighscoretable(util)
                        self.costume.switch("Hammer")
                        self.gotoxy(-41, -311)
                await self.sleep(0)

                await self.yield_()
        if eq(self.costume.name, "White"):
            await self.my_WhiteOutandIn(util, False)
        if eq(self.costume.name, "Background"):
            self.ypos += -1
            while True:
                for _ in range(28):
                    self.ypos += -1

                    await self.yield_()
                self.ypos += 28

                await self.yield_()

    @on_broadcast('splash - hit')
    async def broadcast_splashhit(self, util):
        if gt(self.costume.number, 1):
            self.shown = True
            self.xpos += -8
            await self.sleep(0)
            self.xpos += 12
            await self.sleep(0.06)
            self.xpos += -6
            await self.sleep(0.06)
            self.xpos += 3
            await self.sleep(0.06)
            self.xpos += -1
            await self.sleep(0.06)

    @on_broadcast('splash - hit')
    async def broadcast_splashhit1(self, util):
        if gt(self.costume.number, 6):
            self.var_sy = div((self.costume.number - 4), 2)
            self.costume.set_effect('brightness', -100)
            self.costume.set_effect('ghost', 100)
            self.ypos += (-12 * self.var_sy)
            await self.sleep(0.6)
            await util.sprites["Player"].broadcast_loadhighscore(util)
            util.send_broadcast("Show Score")
            for _ in range(12):
                self.costume.change_effect('ghost', -10)
                self.ypos += self.var_sy

                await self.yield_()
            while not not util.inputs.mouse_down:
                await self.yield_()
            while True:
                if (lt(abs((util.inputs.mouse_x - 45)), 65) and lt(abs((util.inputs.mouse_y - self.var_menuy)), 13)):
                    self.costume.set_effect('brightness', 0)
                    if util.inputs.mouse_down:
                        if eq(self.costume.name, "New Game"):
                            self.sounds.set_effect('pitch', 70)
                            self.sounds.play("menurelease")
                            self.costume.set_effect('ghost', 100)
                            self.costume.switch("white")
                            self.create_clone_of(util, "_myself_")
                            self.costume.switch("New Game")
                            self.costume.set_effect('ghost', 0)
                            return None
                        self.var_t = tonum(("Mute" in self.costume.name))
                        if eq(self.var_t, "true"):
                            self.costume.switch((self.costume.number - 1))
                        else:
                            self.costume.next()
                        if ("Sound Effects" in self.costume.name):
                            util.sprites.stage.var_SFX = str(self.var_t)
                        else:
                            util.sprites.stage.var_COMMENTARY = str(self.var_t)
                        while not not util.inputs.mouse_down:
                            await self.yield_()
                else:
                    self.costume.set_effect('brightness', -100)
                    if util.inputs.mouse_down:
                        while not not util.inputs.mouse_down:
                            await self.yield_()
                await self.sleep(0)

                await self.yield_()
        if eq(self.costume.number, 6):
            await self.sleep(0.6)
            for _ in range(10):
                self.costume.change_effect('ghost', -10)

                await self.yield_()

    @on_broadcast('new game')
    async def broadcast_NewGame(self, util):
        if not eq(self.costume.name, "White"):
            self.shown = False
            self.delete_clone(util)

    @on_broadcast('win')
    async def broadcast_Win(self, util):
        self.costume.switch("black")
        for _ in range(300):
            self.costume.change_effect('ghost', -0.25)

            await self.yield_()

    @on_broadcast('win')
    async def broadcast_Win1(self, util):
        await self.sleep(1)
        self.costume.switch("end title")
        self.create_clone_of(util, "_myself_")
        self.costume.switch("stars")
        self.create_clone_of(util, "_myself_")
        self.costume.switch("black")

    @on_clone_start
    async def clone_start1(self, util):
        if (eq(self.costume.name, "end title") or eq(self.costume.name, "world record")):
            self.gotoxy(0, 0)
            self.costume.set_effect('ghost', 100)
            self.front_layer(util)
            for _ in range(30):
                self.costume.change_effect('ghost', -4)

                await self.yield_()

    @on_broadcast('white out')
    async def broadcast_whiteout1(self, util):
        if eq(self.costume.name, "White"):
            await self.my_WhiteOutandIn(util, not False)

    async def my_WhiteOutandIn(self, util, arg_reset):
        self.front_layer(util)
        for _ in range(10):
            self.costume.change_effect('ghost', -10)

            await self.yield_()
        if arg_reset:
            util.send_broadcast("Reset")
        else:
            util.send_broadcast("New Game")
        self.front_layer(util)
        await self.sleep(0.5)
        for _ in range(50):
            self.costume.change_effect('ghost', 2)

            await self.yield_()

    @on_broadcast('win - record')
    async def broadcast_WinRecord(self, util):
        self.costume.switch("black")
        for _ in range(300):
            self.costume.change_effect('ghost', -0.25)

            await self.yield_()

    @on_broadcast('win - record')
    async def broadcast_WinRecord1(self, util):
        await self.sleep(1)
        self.costume.switch("world record")
        self.create_clone_of(util, "_myself_")
        self.costume.switch("stars")
        self.create_clone_of(util, "_myself_")
        self.costume.switch("black")

    @on_clone_start
    async def clone_start2(self, util):
        if eq(self.costume.name, "stars"):
            util.send_broadcast("time to front")
            self.gotoxy(0, 0)
            self.costume.set_effect('ghost', 100)
            self.back_layer(util)
            for _ in range(30):
                self.costume.change_effect('ghost', -4)
                self.ypos += -1

                await self.yield_()
            while True:
                self.ypos += -1
                if lt(self.ypos, -480):
                    self.ypos += 480

                await self.yield_()


@sprite('Water')
class SpriteWater(Target):
    """Sprite Water"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -436.26
        self._ypos = -152.478150629
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           1, 100, "all around", [
            {
                'name': "Underwater 1-2",
                'path': "eecb593d119d71e3bc7e5206ce8f4b85.svg",
                'center': (494, 104),
                'scale': 1
            },
            {
                'name': "Underwater 2-01",
                'path': "53752ec441ca96fc4a44bfa6a3b96afd.svg",
                'center': (255, 90),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_lx = 0
        self.var_ly = 0



        self.sprite.layer = 12

    @on_broadcast('new game')
    async def broadcast_NewGame(self, util):
        self.gotoxy(0, -180)
        await self.sleep(0.4)
        self.front_layer(util)
        self.change_layer(util, -1)

    @on_broadcast('position level')
    async def broadcast_PositionLevel(self, util):
        self.gotoxy(((((util.timer() * 30) - util.sprites.stage.var_CAMERAX) % 480) - 480), ((-116 + (10 * math.sin(math.radians((util.timer() * 90))))) - div(util.sprites.stage.var_CAMERAY, 1)))


@sprite('Music')
class SpriteMusic(Target):
    """Sprite Music"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 36
        self._ypos = 28
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "costume1",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            12, [
            {
                'name': "Soul_and_Mind 48000 loop",
                'path': "5653e64576a2938e26676aadabec62b5.mp3"
            }
        ])

        self.var_music = 0



        self.sprite.layer = 5

    @on_broadcast('next monologue')
    async def broadcast_nextmonologue(self, util):
        if eq(self.var_music, 0):
            self.var_music = 12
            util.send_broadcast("Start Music")

    @on_broadcast('start music')
    async def broadcast_StartMusic(self, util):
        while not eq(self.var_music, 0):
            if eq(util.sprites["Narrator"].var_talking, 1):
                if lt(self.var_music, 12):
                    self.var_music += 0.2
                    self.sounds.set_volume(self.var_music)
            else:
                if gt(self.var_music, 0):
                    self.var_music += -0.2
                    self.sounds.set_volume(self.var_music)
            await self.sleep(0)

            await self.yield_()

    @on_broadcast('new game')
    async def broadcast_NewGame(self, util):
        self.var_music = 0

    @on_broadcast('start music')
    async def broadcast_StartMusic1(self, util):
        await self.sleep(3)
        self.sounds.set_volume(self.var_music)
        while not not eq(util.sprites["Narrator"].var_talking, 1):
            await self.sounds.play("Soul_and_Mind 48000 loop")

            await self.yield_()
        self.var_music = 0
        self.sounds.set_volume(0)


@sprite('Narrator')
class SpriteNarrator(Target):
    """Sprite Narrator"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "F11",
                'path': "b3c0f8a45e743d229bf2914c3d0e691a.svg",
                'center': (131, 166),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "GOI M1",
                'path': "d6145fe7f8423ecf592ea6e633c8d5ed.wav"
            },
            {
                'name': "GOI M2",
                'path': "671908a655d32a1701d580ba8e753374.mp3"
            },
            {
                'name': "GOI M3",
                'path': "5443e44d9173bdf981d4c2fdfc461ae8.mp3"
            },
            {
                'name': "GOI M4",
                'path': "fd33c57a4bae09ef382f30d87d51e848.mp3"
            },
            {
                'name': "GOI M5",
                'path': "0bf62c0590e554844115fa98cde92a99.mp3"
            },
            {
                'name': "GOI M6",
                'path': "fdc74583ed69799942d4162c46e06663.mp3"
            },
            {
                'name': "GOI M7",
                'path': "7f054e76bcbfb58beb5471851d7b3278.mp3"
            },
            {
                'name': "GOI M8",
                'path': "f267d242d738d5deaecfe0a54cf4e0ed.mp3"
            },
            {
                'name': "GOI M9",
                'path': "753addb3e1887b96da13d15efdef3174.mp3"
            },
            {
                'name': "GOI M10",
                'path': "7e525becaf74a875a7b80971f580dfe8.mp3"
            },
            {
                'name': "GOI M11",
                'path': "6e26e71d864211b283d7766314402ee0.mp3"
            },
            {
                'name': "GOI M12",
                'path': "0c3396560700a252aef37b3c46bfa0cb.mp3"
            },
            {
                'name': "Fall 1",
                'path': "718314909303f167cc2537fbbc4da95c.wav"
            },
            {
                'name': "Fall 2",
                'path': "3accabb338a49460bb33656789280900.wav"
            },
            {
                'name': "Fall 3",
                'path': "91a919e1c000ca023ffb841d29363aac.mp3"
            },
            {
                'name': "Fall 4",
                'path': "6d930e2610ff7a6712f0b3448912a8c2.mp3"
            },
            {
                'name': "Fall 5",
                'path': "c5812d1f6d39cb2b4b135f92d485bac3.wav"
            },
            {
                'name': "Fall 7",
                'path': "38df8cc900e43e03dc83f1a5d3c1c357.mp3"
            },
            {
                'name': "Fall 6",
                'path': "57117bb93743699bcae103751e7fbe4b.mp3"
            },
            {
                'name': "Fall 9",
                'path': "341b260e8884a340fa2218a6d56ca95d.wav"
            },
            {
                'name': "Fall 8",
                'path': "13a139931a59f42a73800e64e146f9b9.mp3"
            },
            {
                'name': "Fall 10",
                'path': "0f4bfbae0a4c3591f8fad31b655970a8.mp3"
            },
            {
                'name': "Fall 11",
                'path': "983436075a98e0248734eb19fc3344a6.mp3"
            },
            {
                'name': "Fall 12",
                'path': "5737f8ecff5788e6f89c57b91952bc06.mp3"
            },
            {
                'name': "Fall 13",
                'path': "0999b28b519d540747e4edd6631b2217.mp3"
            },
            {
                'name': "Fall 14",
                'path': "97f5e2d66a1d82e3f479668bcdc461c5.mp3"
            },
            {
                'name': "Fall 15",
                'path': "a04a82db32b15bc958227c6dfaedce8c.mp3"
            },
            {
                'name': "Fall 16",
                'path': "e9ec98c71233a574133c2aeedcb3e12a.mp3"
            },
            {
                'name': "Fall 17",
                'path': "14dce4b51f71399af30d0129252a87db.mp3"
            },
            {
                'name': "Fall 18",
                'path': "8f9da1a1b385fd30a64189c3af4a85f7.mp3"
            },
            {
                'name': "Fall 19",
                'path': "423bcf93f0b45f7ce9bf5919972d17e4.mp3"
            },
            {
                'name': "Fall 20",
                'path': "f65015d4c9b0d011dce3e98330c85ab0.mp3"
            },
            {
                'name': "Fall 21",
                'path': "9ae625317bb33ab683645fbeca14ba71.mp3"
            },
            {
                'name': "Fall 22",
                'path': "6a4a9b31ac99a02f11fa49de05f55a0b.mp3"
            },
            {
                'name': "Fall 23",
                'path': "4d144ed719b115453c29576901db82eb.mp3"
            },
            {
                'name': "Fall 24",
                'path': "2e4955c47db6946e9790a90374ffcf75.mp3"
            }
        ])

        self.var_talking = 0
        self.var_scriptno = 0
        self.var_readuntil = 0
        self.var_fallcount = 0
        self.var_lmx = -232
        self.var_lmy = 180
        self.var_stuck = 7
        self.var_fullscreenissue = 0

        self.list_fullscreenremind = StaticList(
            [10, 40, 150, 500, 1000]
        )

        self.sprite.layer = 7

    @on_broadcast('new game')
    async def broadcast_NewGame(self, util):
        self.var_talking = 0
        self.var_scriptno = 0
        self.var_readuntil = 0
        self.var_fallcount = 0
        self.var_stuck = 0
        self.var_fullscreenissue = 0
        self.shown = False

    @on_broadcast('position level')
    async def broadcast_PositionLevel(self, util):
        await self.my_DetectMouseIssues(util, )
        if gt(util.sprites.stage.var_PLAYERY, 10938):
            await self.my_talkto(util, 12)
        else:
            if gt(util.sprites.stage.var_PLAYERY, 9300):
                await self.my_talkto(util, 11)
            else:
                if gt(util.sprites.stage.var_PLAYERY, 8380):
                    await self.my_talkto(util, 10)
                else:
                    if gt(util.sprites.stage.var_PLAYERY, 7180):
                        await self.my_talkto(util, 9)
                    else:
                        if (gt(util.sprites.stage.var_PLAYERY, 5633) and lt(util.sprites.stage.var_PLAYERX, 2183)):
                            await self.my_talkto(util, 8)
                        else:
                            if gt(util.sprites.stage.var_PLAYERY, 5330):
                                await self.my_talkto(util, 7)
                            else:
                                if (gt(util.sprites.stage.var_PLAYERY, 4427) and gt(util.sprites.stage.var_PLAYERX, 2583)):
                                    await self.my_talkto(util, 6)
                                else:
                                    if (gt(util.sprites.stage.var_PLAYERY, 3710) and lt(util.sprites.stage.var_PLAYERX, 1960)):
                                        await self.my_talkto(util, 5)
                                    else:
                                        if gt(util.sprites.stage.var_PLAYERY, 2993):
                                            await self.my_talkto(util, 4)
                                        else:
                                            if gt(util.sprites.stage.var_PLAYERY, 1733):
                                                await self.my_talkto(util, 3)
                                            else:
                                                if (gt(util.sprites.stage.var_PLAYERX, 2062) and gt(util.sprites.stage.var_PLAYERY, 244)):
                                                    await self.my_talkto(util, 2)
                                                else:
                                                    if (gt(util.sprites.stage.var_PLAYERX, 1500) and gt(util.sprites.stage.var_PLAYERY, 254)):
                                                        await self.my_talkto(util, 1)
                                                    else:
                                                        pass
        if (gt(self.var_talking, 0) or eq(util.sprites.stage.var_COMMENTARY, "false")):
            return None
        if lt(self.var_scriptno, self.var_readuntil):
            self.var_scriptno += 1
            util.send_broadcast("next monologue")

    @on_broadcast('next monologue')
    async def broadcast_nextmonologue(self, util):
        self.var_talking = 1
        await self.sounds.play(("GOI M" + str(self.var_scriptno)))
        self.var_talking = 0

    @on_broadcast('fall')
    async def broadcast_fall(self, util):
        if eq(util.sprites.stage.var_COMMENTARY, "true"):
            self.var_fallcount += 1
            if lt(self.var_fallcount, 25):
                self.var_talking = 2
                await self.sounds.play(("Fall " + str(self.var_fallcount)))
                self.var_talking = 0

    @warp
    async def my_DetectMouseIssues(self, util, ):
        if (eq(util.inputs.mouse_x, self.var_lmx) and eq(util.inputs.mouse_y, self.var_lmy)):
            if gt(abs(util.inputs.mouse_y), 170):
                self.var_stuck += 1
            return None
        if gt(self.var_stuck, 3):
            if gt(abs((util.inputs.mouse_x - self.var_lmx)), 100):
                self.var_fullscreenissue += 1
                if self.var_fullscreenissue in self.list_fullscreenremind:
                    util.send_broadcast("F11 reminder")
        self.var_lmx = util.inputs.mouse_x
        self.var_lmy = util.inputs.mouse_y
        self.var_stuck = 0

    @warp
    async def my_talkto(self, util, arg_part):
        if gt(arg_part, self.var_readuntil):
            self.var_readuntil = arg_part

    @on_broadcast('f11 reminder')
    async def broadcast_f11reminder(self, util):
        if eq(util.sprites.stage.var_COMMENTARY, "true"):
            self.gotoxy(0, 0)
            self.costume.switch("F11")
            for _ in range(3):
                self.shown = True
                await self.sleep(0.5)
                self.shown = False
                await self.sleep(0.3)

                await self.yield_()
            self.shown = True
            await self.sleep(16)
            self.shown = False


@sprite('Timer')
class SpriteTimer(Target):
    """Sprite Timer"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 118
        self._ypos = 154
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 40, "all around", [
            {
                'name': "d",
                'path': "3495321c6b96977754d0640a217b0bbb.png",
                'center': (0, 0),
                'scale': 2
            },
            {
                'name': "d0",
                'path': "64b59074f24d0e2405a509a45c0dadba.svg",
                'center': (29, 39),
                'scale': 1
            },
            {
                'name': "d1",
                'path': "9f75c26aa6c56168a3e5a4f598de2c94.svg",
                'center': (24, 39),
                'scale': 1
            },
            {
                'name': "d2",
                'path': "e8d8bf59db37b5012dd643a16a636042.svg",
                'center': (28, 41),
                'scale': 1
            },
            {
                'name': "d3",
                'path': "57f7afe3b9888cca56803b73a62e4227.svg",
                'center': (33, 42),
                'scale': 1
            },
            {
                'name': "d4",
                'path': "b8209e1980475b30ff11e60d7633446d.svg",
                'center': (31, 38),
                'scale': 1
            },
            {
                'name': "d5",
                'path': "aacb5b3cec637f192f080138b4ccd8d2.svg",
                'center': (30, 38),
                'scale': 1
            },
            {
                'name': "d6",
                'path': "84d9f26050c709e6b98706c22d2efb3d.svg",
                'center': (30, 37),
                'scale': 1
            },
            {
                'name': "d7",
                'path': "6194b9a251a905d0001a969990961724.svg",
                'center': (31, 42),
                'scale': 1
            },
            {
                'name': "d8",
                'path': "55e95fb9c60fbebb7d20bba99c7e9609.svg",
                'center': (31, 37),
                'scale': 1
            },
            {
                'name': "d9",
                'path': "0f53ee6a988bda07cba561d38bfbc36f.svg",
                'center': (28, 36),
                'scale': 1
            },
            {
                'name': "d'",
                'path': "091a881fcfe0b80a5f76615792b563b7.svg",
                'center': (11, 38),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_id = 5
        self.var_cost = "d"



        self.sprite.layer = 15

    @on_broadcast('splash - hit')
    async def broadcast_splashhit(self, util):
        self.shown = False
        self.costume.switch("d0")
        self.costume.size = 40
        await self.sleep(0.5)
        self.front_layer(util)
        self.var_id = 1
        self.gotoxy(220, 154)
        self.create_clone_of(util, "_myself_")
        self.var_id = 2
        self.xpos += -21
        self.create_clone_of(util, "_myself_")
        self.var_id = -3
        self.xpos += -15
        self.costume.switch("d'")
        self.create_clone_of(util, "_myself_")
        self.var_id = 3
        self.xpos += -15
        self.costume.switch("d0")
        self.create_clone_of(util, "_myself_")
        self.var_id = 4
        self.xpos += -21
        self.costume.switch("d")
        self.create_clone_of(util, "_myself_")
        self.var_id = -5
        self.xpos += -15
        self.create_clone_of(util, "_myself_")
        self.var_id = 5
        self.xpos += -15

    @on_broadcast('position level')
    async def broadcast_PositionLevel(self, util):
        await self.my_char(util, util.sprites.stage.list_TIME[abs(self.var_id)])

    async def my_char(self, util, arg_c):
        if lt(self.var_id, 0):
            if eq(arg_c, ""):
                self.var_cost = "d"
            else:
                self.var_cost = "d'"
        else:
            self.var_cost = ("d" + str(arg_c))
        if not eq(self.var_cost, self.costume.name):
            self.costume.switch(self.var_cost)

    @on_broadcast('show score')
    async def broadcast_showscore1(self, util):
        self.costume.set_effect('ghost', 100)
        self.shown = True
        await self.my_char(util, util.sprites.stage.list_TIME[abs(self.var_id)])
        for _ in range(10):
            self.costume.change_effect('ghost', -10)

            await self.yield_()

    @on_broadcast('time to front')
    async def broadcast_timetofront1(self, util):
        self.front_layer(util)


@sprite('Cloud List')
class SpriteCloudList(Target):
    """Sprite Cloud List"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "lower",
                'path': "bf5503eefe151ba0d3212b0f3dc8bc56.svg",
                'center': (-88, -136),
                'scale': 1
            },
            {
                'name': "A_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "B_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "C_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "D_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "E_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "F_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "G_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "H_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "I_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "J_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "K_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "L_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "M_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "N_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "O_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "P_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "Q_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "R_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "S_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "T_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "U_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "V_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "W_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "X_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "Y_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': "Z_",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_letter = 696
        self.var_encoded = 54292718201463636567656900415434818281263646566004161628122710291217632600416833910311828656800417164310272734765124292914273400418183657561127242800418193827182228242373481014212829272422004184869665366670041849271423286400418996468103114273419004199711273023241332182211100042039112411102210151828170042077111829122413146362620042102431027273476103114273419004212043102727347610311427341900421203817182576401029142776636465004212922715232124311427640214241407650151518121810210042198541227102912171427372434350042235733818221423102918127300422364026390042250132218292734636465640042290551714382421101114270042294122118122014271624231428004231523242373161423142718122800423256642646263700042340
        self.var_value = 2340
        self.var_idx = "4"
        self.var_c = "042235733818221423102918127300422364026390042250132218292734636465640042290551714382421101114270042294122118122014271624231428004231523242373161423142718122800423256642646263700042340"
        self.var_cvarid = 51
        self.var_lockid = 9235639673

        self.list_codes = StaticList(
            ["", "", "", "", "", "", "", "", "", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "+", "-", ".", " ", "_"]
        )
        self.list_cloudout = List(
            [5429271820146363656765690041543481828126364656600416162812271029121763260041683391031182865680041716431027273476512429291427340041818365756112724280041819382718222824237348101421282927242200418486966536667004184927142328640041899646810311427341900419971127, 3023241332182211100042039112411102210151828170042077111829122413146362620042102431027273476103114273419004212043102727347610311427341900421203817182576401029142776636465004212922715232124311427640214241407650151518121810210042198541227102912171427372434350, "042235733818221423102918127300422364026390042250132218292734636465640042290551714382421101114270042294122118122014271624231428004231523242373161423142718122800423256642646263700042340"]
        )

        self.sprite.layer = 14

    @warp
    async def my_writetoencoded(self, util, arg_val):
        self.var_letter = 1
        for _ in range(len(str(arg_val))):
            self.var_c = letter_of(str(arg_val), toint(self.var_letter))
            self.costume.switch((self.var_c + "_"))
            self.var_c = str(self.list_codes.index(self.var_c))
            if eq(self.costume.name, "lower"):
                self.var_encoded = (str(self.var_encoded) + self.var_c)
            else:
                self.var_encoded = (str(self.var_encoded) + str((tonum(self.var_c) + 26)))
                self.costume.switch("lower")
            self.var_letter += 1
        self.var_encoded = (str(self.var_encoded) + "00")

    @warp
    async def my_valuereadfromencoded(self, util, ):
        self.var_value = ""
        while True:
            self.var_idx = (letter_of(str(self.var_encoded), toint(self.var_letter)) + letter_of(str(self.var_encoded), toint((self.var_letter + 1))))
            self.var_letter += 2
            if lt(self.var_idx, 1):
                return None
            self.var_value = (str(self.var_value) + str(self.list_codes[toint(self.var_idx)]))

    @warp
    async def my_BeginEncodeDecode(self, util, arg_encoded):
        self.var_encoded = arg_encoded
        self.var_letter = 1

    @on_green_flag
    async def green_flag(self, util):
        self.costume.switch("lower")
        self.shown = False

    @on_broadcast('cloud list - save')
    async def broadcast_cloudlistsave(self, util):
        self.shown = False
        await self.my_Save(util, )
        self.shown = True
        await self.my_writetocloud(util, 0.1)
        self.shown = False

    @warp
    async def my_writenumbertoencoded(self, util, arg_val):
        self.var_encoded = (str(self.var_encoded) + (str(len(str(arg_val))) + str(arg_val)))

    @on_broadcast('cloud list - load')
    async def broadcast_cloudlistload(self, util):
        await self.my_Load(util, )

    @warp
    async def my_Save(self, util, ):
        await self.my_BeginEncodeDecode(util, "")
        self.var_cvarid = 1
        for _ in range(toint(div(len(util.sprites.stage.list_CLOUDLIST), 2))):
            await self.my_writetoencoded(util, util.sprites.stage.list_CLOUDLIST[toint(self.var_cvarid)])
            self.var_cvarid += 1
            await self.my_writenumbertoencoded(util, util.sprites.stage.list_CLOUDLIST[toint(self.var_cvarid)])
            self.var_cvarid += 1
        self.var_idx = "1"
        self.list_cloudout.delete_all()
        self.var_c = ""
        for _ in range(len(str(self.var_encoded))):
            self.var_c = (self.var_c + letter_of(str(self.var_encoded), toint(self.var_idx)))
            self.var_idx = str(tonum(self.var_idx) + 1)
            if gt(len(self.var_c), 255):
                self.list_cloudout.append(self.var_c)
                self.var_c = ""
        if gt(len(self.var_c), 0):
            self.list_cloudout.append(self.var_c)

    async def my_writetocloud(self, util, arg_wait):
        util.sprites.stage.var_cloudlock = self.var_lockid
        await self.sleep(arg_wait)
        if not eq(("a" + str(util.sprites.stage.var_cloudlist1)), ("a" + str(self.list_cloudout[1]))):
            util.sprites.stage.var_cloudlist1 = self.list_cloudout[1]
            await self.sleep(arg_wait)
        if not eq(("a" + str(util.sprites.stage.var_cloudlist2)), ("a" + str(self.list_cloudout[2]))):
            util.sprites.stage.var_cloudlist2 = self.list_cloudout[2]
            await self.sleep(arg_wait)
        if not eq(("a" + str(util.sprites.stage.var_cloudlist3)), ("a" + str(self.list_cloudout[3]))):
            util.sprites.stage.var_cloudlist3 = self.list_cloudout[3]
            await self.sleep(arg_wait)
        if not eq(("a" + str(util.sprites.stage.var_cloudlist4)), ("a" + str(self.list_cloudout[4]))):
            util.sprites.stage.var_cloudlist4 = self.list_cloudout[4]
            await self.sleep(arg_wait)
        if not eq(("a" + str(util.sprites.stage.var_cloudlist5)), ("a" + str(self.list_cloudout[5]))):
            util.sprites.stage.var_cloudlist5 = self.list_cloudout[5]
            await self.sleep(arg_wait)
        if not eq(("a" + str(util.sprites.stage.var_cloudlist6)), ("a" + str(self.list_cloudout[6]))):
            util.sprites.stage.var_cloudlist6 = self.list_cloudout[6]
            await self.sleep(arg_wait)
        if not eq(("a" + str(util.sprites.stage.var_cloudlist7)), ("a" + str(self.list_cloudout[7]))):
            util.sprites.stage.var_cloudlist7 = self.list_cloudout[7]
            await self.sleep(arg_wait)

    @warp
    async def my_valuereadnumberfromencoded(self, util, ):
        self.var_value = ""
        self.var_idx = letter_of(str(self.var_encoded), toint(self.var_letter))
        if eq(self.var_idx, ""):
            return None
        self.var_letter += 1
        for _ in range(toint(self.var_idx)):
            self.var_value = (str(self.var_value) + letter_of(str(self.var_encoded), toint(self.var_letter)))
            self.var_letter += 1

    @warp
    async def my_Load(self, util, ):
        util.sprites.stage.list_CLOUDLIST.delete_all()
        self.var_encoded = util.sprites.stage.var_cloudlist1
        self.var_encoded = (str(self.var_encoded) + str(util.sprites.stage.var_cloudlist2))
        self.var_encoded = (str(self.var_encoded) + str(util.sprites.stage.var_cloudlist3))
        self.var_encoded = (str(self.var_encoded) + str(util.sprites.stage.var_cloudlist4))
        self.var_encoded = (str(self.var_encoded) + str(util.sprites.stage.var_cloudlist5))
        self.var_encoded = (str(self.var_encoded) + str(util.sprites.stage.var_cloudlist6))
        self.var_encoded = (str(self.var_encoded) + str(util.sprites.stage.var_cloudlist7))
        await self.my_BeginEncodeDecode(util, self.var_encoded)
        while not gt(self.var_letter, len(str(self.var_encoded))):
            await self.my_valuereadfromencoded(util, )
            util.sprites.stage.list_CLOUDLIST.append(self.var_value)
            await self.my_valuereadnumberfromencoded(util, )
            util.sprites.stage.list_CLOUDLIST.append(self.var_value)

    @on_broadcast('cloud - lock')
    async def broadcast_CLOUDLOCK(self, util):
        self.var_lockid = pick_rand(0, 10000000000)
        while True:
            await self.my_readlock(util, util.sprites.stage.var_cloudlock)
            self.var_value = self.var_encoded
            self.var_encoded = ""
            while not eq(self.var_value, self.var_encoded):
                await self.sleep(0.7)
                await self.my_readlock(util, util.sprites.stage.var_cloudlock)

                await self.yield_()
            util.sprites.stage.var_cloudlock = self.var_lockid
            await self.my_readlock(util, self.var_lockid)
            self.var_value = self.var_encoded
            await self.sleep(0.7)
            await self.my_readlock(util, util.sprites.stage.var_cloudlock)
            if eq(self.var_value, self.var_encoded):
                util.sprites.stage.var_cloudlock = self.var_lockid
                self.stop_other()
                self.shown = True
                return None
            await self.sleep(pick_rand(0, 2))

            await self.yield_()

    @warp
    async def my_readlock(self, util, arg_lock):
        self.var_encoded = ("lock" + str(util.sprites.stage.var_cloudlist2))
        self.var_encoded = (str(self.var_encoded) + str(util.sprites.stage.var_cloudlist2))
        self.var_encoded = (str(self.var_encoded) + str(util.sprites.stage.var_cloudlist3))
        self.var_encoded = (str(self.var_encoded) + str(util.sprites.stage.var_cloudlist4))
        self.var_encoded = (str(self.var_encoded) + str(util.sprites.stage.var_cloudlist5))
        self.var_encoded = (str(self.var_encoded) + str(util.sprites.stage.var_cloudlist6))
        self.var_encoded = (str(self.var_encoded) + str(util.sprites.stage.var_cloudlist7))
        self.var_encoded = (str(self.var_encoded) + str(arg_lock))

    @on_broadcast('cloud - lock')
    async def broadcast_CLOUDLOCK1(self, util):
        self.costume.switch("lower")
        self.shown = True
        self.gotoxy(0, 0)
        self.front_layer(util)
        while True:
            await self.sleep(0.7)
            self.shown = False
            await self.sleep(0.3)
            self.shown = True

            await self.yield_()


@sprite('High Score')
class SpriteHighScore(Target):
    """Sprite High Score"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 36
        self._ypos = 28
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "costume1",
                'path': "3339a2953a3bf62bb80e54ff575dbced.svg",
                'center': (0, 0),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_i = 51
        self.var_format = "1'18 ... 4G2018"
        self.var_t = 0
        self.var_tx = 0
        self.var_invalidate = "true"

        self.list_TOP25 = List(
            ["0'51 ... Strike113537", "0'53 ... Misc1234", "0'56 ... scratch1q", "0'57 ... Davis36", "1'00 ... Harry_Pottery", "1'00 ... AVUbros", "1'01 ... Crimson-Maelstrom", "1'01 ... 74R45", "1'03 ... rens2", "1'06 ... 26averyj", "1'07 ... brunodwimba", "1'09 ... bobamafish", "1'10 ... bitcode100", "1'10 ... Harry_averyj", "1'10 ... Harry_averyj", "1'10 ... Chip_Eater_123", "1'13 ... m9QwcHbG_ElGFE_Official", "1'14 ... ScratcherBoyz", "1'14 ... -Cimenatic-", "1'15 ... EqD", "1'16 ... dmitry1232", "1'16 ... TheColaber", "1'17 ... clickergones", "1'17 ... non-generics", "1'18 ... 4G2018"]
        )

        self.sprite.layer = 8

    @on_broadcast('show high score table')
    async def broadcast_showhighscoretable(self, util):
        await util.sprites["Cloud List"].broadcast_cloudlistload(util)
        await self.my_ShowTop10(util, )

    @warp
    async def my_ShowTop10(self, util, ):
        self.list_TOP25.delete_all()
        self.var_i = 1
        for _ in range(25):
            await self.my_format(util, self.var_i)
            self.list_TOP25.append(self.var_format)
            self.var_i += 2
        self.list_TOP25.show()

    @warp
    async def my_format(self, util, arg_i):
        self.var_format = util.sprites.stage.list_CLOUDLIST[toint(arg_i)]
        if eq(self.var_format, ""):
            return None
        self.var_format = (" ... " + str(self.var_format))
        await self.my_prependformatwith(util, util.sprites.stage.list_CLOUDLIST[toint((arg_i + 1))])

    @warp
    async def my_prependformatwith(self, util, arg_time):
        self.var_t = math.floor(div(arg_time, 30))
        self.var_tx = (self.var_t % 60)
        self.var_t = math.floor(div(self.var_t, 60))
        if lt(self.var_tx, 10):
            self.var_format = (("0" + str(self.var_tx)) + str(self.var_format))
        else:
            self.var_format = ((letter_of(str(self.var_tx), 1) + letter_of(str(self.var_tx), 2)) + str(self.var_format))
        self.var_tx = (self.var_t % 60)
        self.var_t = math.floor(div(self.var_t, 60))
        self.var_format = ("'" + str(self.var_format))
        if lt(self.var_tx, 10):
            if gt(self.var_t, 0):
                self.var_format = (("0" + str(self.var_tx)) + str(self.var_format))
            else:
                self.var_format = (str(self.var_tx) + str(self.var_format))
        else:
            self.var_format = ((letter_of(str(self.var_tx), 1) + letter_of(str(self.var_tx), 2)) + str(self.var_format))
        self.var_tx = (self.var_t % 60)
        if gt(self.var_t, 0):
            self.var_format = ("'" + str(self.var_format))
            self.var_format = ((str(self.var_tx) + "'") + str(self.var_format))

    @on_broadcast('save time to cloud')
    async def broadcast_savetimetocloud(self, util):
        util.sprites.stage.var_LATEST = util.sprites.stage.var_FRAME
        if (lt(toint(util.sprites.stage.var_FASTEST), 10) or lt(util.sprites.stage.var_FRAME, util.sprites.stage.var_FASTEST)):
            await self.sleep(0.1)
            util.sprites.stage.var_FASTEST = util.sprites.stage.var_FRAME
            util.send_broadcast("Win - Record")
        else:
            util.send_broadcast("Win")
        await util.sprites["Cloud List"].broadcast_cloudlistload(util)
        self.var_invalidate = ""
        await self.my_SavetoTop10(util, config.USERNAME, util.sprites.stage.var_FRAME)
        if gt(self.var_invalidate, 0):
            await self.sleep(0.1)
            await util.send_broadcast_wait("CLOUD - LOCK")
            await util.sprites["Cloud List"].broadcast_cloudlistload(util)
            await self.my_savetocloud(util, config.USERNAME, util.sprites.stage.var_FRAME)

    async def my_savetocloud(self, util, arg_user, arg_time):
        self.var_invalidate = ""
        await self.my_SavetoTop10(util, arg_user, arg_time)
        if gt(self.var_invalidate, 0):
            await util.sprites["Cloud List"].broadcast_cloudlistsave(util)

    @warp
    async def my_SavetoTop10(self, util, arg_user, arg_time):
        self.var_i = 1
        for _ in range(25):
            if (eq(util.sprites.stage.list_CLOUDLIST[toint(self.var_i)], "") or lt(arg_time, util.sprites.stage.list_CLOUDLIST[toint((self.var_i + 1))])):
                util.sprites.stage.list_CLOUDLIST.insert(toint(self.var_i), arg_time)
                util.sprites.stage.list_CLOUDLIST.insert(toint(self.var_i), arg_user)
                self.var_i += 2
                while not (gt(self.var_i, 50) or eq(util.sprites.stage.list_CLOUDLIST[toint(self.var_i)], arg_user)):
                    self.var_i += 2
                util.sprites.stage.list_CLOUDLIST.delete(toint(self.var_i))
                util.sprites.stage.list_CLOUDLIST.delete(toint(self.var_i))
                self.var_invalidate = "true"
                return None
            if eq(util.sprites.stage.list_CLOUDLIST[toint(self.var_i)], arg_user):
                return None
            self.var_i += 2

    @warp
    async def my_Savelast25(self, util, arg_user, arg_time):
        while not gt(len(util.sprites.stage.list_CLOUDLIST), 20):
            util.sprites.stage.list_CLOUDLIST.append("")
        self.var_i = 21
        while not gt(self.var_i, len(util.sprites.stage.list_CLOUDLIST)):
            if eq(util.sprites.stage.list_CLOUDLIST[toint(self.var_i)], arg_user):
                util.sprites.stage.list_CLOUDLIST.delete(toint(self.var_i))
                util.sprites.stage.list_CLOUDLIST.delete(toint(self.var_i))
            else:
                self.var_i += 2
        util.sprites.stage.list_CLOUDLIST.insert(21, arg_time)
        util.sprites.stage.list_CLOUDLIST.insert(21, arg_user)
        util.sprites.stage.list_CLOUDLIST.delete(toint(((35 * 2) + 1)))
        util.sprites.stage.list_CLOUDLIST.delete(toint(((35 * 2) + 1)))

    @on_green_flag
    async def green_flag(self, util):
        self.list_TOP25.hide()

    @on_broadcast('new game')
    async def broadcast_NewGame(self, util):
        self.list_TOP25.hide()

    @on_broadcast('hide highscore table')
    async def broadcast_hidehighscoretable(self, util):
        self.list_TOP25.hide()




if __name__ == '__main__':
    engine.start_program()
