# special
define quote = nvl_narrator
define comment = Character("COMMENT") # XXX delete this before release
define n = Character("", what_prefix="{i}", what_suffix="{/i}")
# residents
define misato = Character("Umeji Misato") # room 4
define trust_player=0
define akane = Character("Akane") # room 3
define trust_akane=5
define yuuko = Character("Hinamori Yuuko") # room 2
define trust_yuuko=0
define miko = Character("Umeji Miko") # room 1
define trust_miko=25
define hanabi = Character("Tamaya Hanabi") # room 8
define trust_hanabi=0
define hikari = Character("Asahara Hikari") # room 7
define trust_hikari=0
define akiko = Character("Ikuhara Akiko") # room 6
define trust_akiko=0
define corto = Character("Master Corto") # penthouse
define cat_affinity=0 # secret basement
# other
define mina = Character("Umeji Mina")
define trust_mina=25
define kuroki = Character("Fyodor Federov Kuroki")
define trust_kuroki=0
define ai = Character("Akagi Ai")
define trust_ai=0
define aoi = Character("Tomoe Aoi")
define trust_aoi=0

# phone versions, for people we talk to on the phone
define mina_phone = Character("Umeji Mina (SMS)", what_prefix="{k=1.5}", what_suffix="{/k}") # TODO: replace with monospace font

init -2 python:
    class generateAffinityContent:
        def __call__(self):
            def bargraph(pct):
                pct=min(pct, 100)
                color="#f00"
                if pct>25:
                    color="#0f0"
                    if pct>75:
                        color="#00f"
                bar="#"*(int(pct/10))
                bar+=(" "*(10-int(pct/10)))
                return "{color="+color+"}"+bar+" "+str(pct)+"%{/color}"

            ret=[]
            ret.append("Player: "+bargraph(trust_player)+"%")
            ret.append("")
            ret.append("Akane: "+bargraph(trust_akane)+"%")
            ret.append("Yuuko: "+bargraph(trust_yuuko)+"%")
            ret.append("Miko: "+bargraph(trust_miko)+"%")
            ret.append("Hanabi: "+bargraph(trust_hanabi)+"%")
            ret.append("Hikari: "+bargraph(trust_hikari)+"%")
            ret.append("Akiko: "+bargraph(trust_akiko)+"%")
            ret.append("")
            ret.append("Mina: "+bargraph(trust_mina)+"%")
            ret.append("Kuroki: "+bargraph(trust_kuroki)+"%")
            ret.append("Ai: "+bargraph(trust_ai)+"%")
            ret.append("Aoi: "+bargraph(trust_aoi)+"%")
            ret.append("")
            ret.append("Cats: "+bargraph(cat_affinity)+"%")
            return "\n".join(ret)
        def __str__(self):
            self.call()

screen affinity:
    tag menu
    use game_menu(_("Affinity"), scroll="viewport"):
        style_prefix "about"
        vbox:
            label _("Affinity:")
            label (generateAffinityContent()())
