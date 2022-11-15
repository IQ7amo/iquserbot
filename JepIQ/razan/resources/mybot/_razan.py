from jepthon.Config import Config
from jepthon.plugins import mention

RAZAN = Config.TG_BOT_USERNAME
# for alive
ROZ = (
    f"**⌯︙بۆتی زیرەك سەرکەوتوانە کاردەکات 🤍،**\n"
    f"**   - وەشانی تێلثۆن :** `1.23.0\n`"
    f"**   - وەشانی بۆتی زیرەك :** `4.0.1`\n"
    f"**   - بۆتێکی بەکارهاتوو :** `{RAZAN}`\n"
    f"**   - وەشانی پایثۆن :** `3.9.6\n`"
    f"**   - بەکارهێنەر :** {mention}\n"
)
# فەرمانی یارمەتیدەر
BBACK = "**-لیستی فەرمانەکانی سەرچاوەی بۆتی زیرەك یەکێك لە هەڵبژاردەکانی خوارەوە هەڵبژێرە🕷️🖤**"
ROZBOT = "**•❒ فەرمانی بۆت🕷️🖤**\n\n( `.سەرچاوە ` ) \n• بۆ بینینی زانیاری سەرچاوە\n\n(  `.پشکنین`  ) \n. بۆ بینینی زانیاری دامەزراندنەکەت \n\nٴ╼──────────────────╾\n\n( `.دامەزراندن`  ) \n• بە وەڵامدانەوەی فایلێك بۆ دامەزراندنی لە سەرچاوەکە \n\n( `.لابردنی دامەزرادن < ناوی فایلەکە >`  )  \n• بۆ لابردنی فایلی دامەزراو لە سەرچاوەکە  -  بەبێ مۆد  < >\n\nٴ╼──────────────────╾\n\n( `.نوێکردنەوە`  )\n• بۆ نوێکردنەوەی فایلی سەرچاوەکان ئەگەر نوێکردنەوەیەك لە گەشەپێدەرەکانەوە دابەزێت\n\n( `.دووبارە کارپێکردن` ) \n• دووبارە کارپێکردنی بۆتەکە ئەگەر کێشەیەك هەبوو لە بۆت ئەم فەرمانە بەکاربهێنە\n\nٴ╼──────────────────╾ \n\n( `.ڤار `) \n. بۆ بینینی زانیاری دامەزراندنەکەت لە ئەیپی هاش و کۆدی تێرمۆکس ئەم فەرمانە لە گرووپ بەکارمەهێنە و هاوبەشی پێ مەکە\n\nٴ╼──────────────────╾\n\n( `.چی کاتێك`  ) \n• بە وەڵامدانەوەی نامە بۆ زانینی بەرواری گواستنەوەکەی و کاتی گواستنەوەکەی\n\nٴ╼──────────────────╾ \n\n( `.فایلەکان`  ) \n• بۆ بینینی هەموو ناوی فایلەکانی سەرچاوەکە\n\nٴ╼──────────────────╾ \n@xv7amo  -  @IQ7amo"
ROZSEG = "**•❒ فەرمانی گۆڕینی مەبەستەکان و فۆڕماتەکان🕷️🖤**\n\n( `.گۆڕینی ستیکەر` ) \n• بە وەڵامدانەوەی ئەو ستیکەرە گۆڕینی بۆ وێنە \n\n( `.گۆڕینی وێنە` ) \n• بە وەڵامدانەوەی ئەو وێنەیە گۆڕینی بۆ ستیکەر\n\n( `.گۆڕینی mp3` )\n• بە وەڵامدانەوەی ئەو گۆرانیەی کە دەتەوێ بیگۆڕی بۆ نامەی دەنگی، دەنگ\n\n( `.گۆڕینی voice` )\n•  گۆڕینی دەنگ، نامەی دەنگی .. بۆ mp3 \n\n( `.گۆڕینی ڤیدیۆ` ) \n•  بە وەڵامدانەوەی ئەو ڤیدیۆیە بۆ گۆڕینی بۆ گیف gif\n\nٴ╼──────────────────╾\n\n( `.ئادد + بەستەری گرووپ` ) \n• بەکارهێنانی ئەم فەرمانە بۆ زیادکردنی ئەندامە دەبێت ئەم فەرمانە بنووسی لەگەڵ بەستەری گرووپەکە، بەڵام ئەبێت گشتی بێت\n\n( `.ناردنی گشتی` ) \n• بە وەڵامدانەوەی وێنەیەك یان دەقێك ڕاستەوخۆ دەینێرێتە هەموو گرووپەکان \n\n( `.دەورووبەر` ) \n• فەرمانەکە دەنووسیت لەگەڵ دەقێك وەدواتر دەنێردرێت بۆ هەموو ئەو کەسانەی لە ئەکاونتتدا هەن\n\nٴ╼──────────────────╾\n@xv7amo  - @IQ7amo"
ROZPRV = "•❒ فەرمانی پاراستنی تایبەت🕷️🖤\n\n( `.پاراستن` چالاککردن/ناچالاککردن ) \n• بۆ چالاککردن و ناچالاککردنی فەرمانی پاراستن لە تایبەت \n\n( `.مۆڵەت` ) \n• بەوەڵامدانەوەی ئەو کەسە کە ڕێگەبدەی لە تایبەت قسەبکات\n\n( `.ڕەتکردنەوە` ) \n• بالرد بە وەڵامدانەوەی ئەو کەسە کە ڕەتیبکەیەوە لە تایبەت قسەبکات \n\n( `.ڕێگەپێدراوەکان` )\n•بە ناردنی ئەم فەرمانە هەموو ئەو کەسانە ئەبینی کە ڕێگەتداوە یان ڕەتتکردۆتەوە🕷️.\n\nٴ╼──────────────────╾\n\n( `.تێلەگراف میدیا` ) \n• بە وەڵامدانەوەی وێنەیەك بۆ دەستکەوتنی بەستەرێك بۆ وێنەکە بۆ بەکارهێنانی لە ڤارەکە\n\n( `.تێلەگراف دەق` ) \n• بالرد بە وەڵامدانەوەی وتارێك یان دەقێك لە فەرمانەکەدا بۆ دەستکەوتنی بەستەرێك بۆ وتارەکە\n\nٴ╼──────────────────╾ \n\n( `.تایبەت <ناوی بەکارهێنەر><نامە>` )\n• ئەم فەرمانە بەکاردێت بۆ ناردنی نامەیەك بۆ کەسێك لە ڕێگای یوزەر نەیم|ناوی بەکارهێنەر لە هەرشوێنێک بێت🕷️."
ROZADM = "**•❒ فەرمانی بەڕێوبەر🕷️🖤**\n\n( `.دەرکردن` ) \n• وەڵامی کەسێك دەدەیتەوە یان ناوی بەکارهێنەر|یوزەر نەیم لەگەڵ فەرمانەکە بەکار ئەهێنیت بۆ دەرکردنی\n\n( `.لادانی دەرکردن` )\n• بە وەڵامدانەوە یان نوسینی ناوی بەکارهێنەر لەگەڵ فەرمانەکە بۆ لادانی دەرکردن لەسەر کەسەکە\n\nٴ╼──────────────────╾\n\n( `.ئاگاداری` ) \n• وەڵامی کەسێك دەدەیتەوە یان ناوی بەکارهێنەر لەگەڵ فەرمانەکە بەکارئەهێنیت بۆ بێدەنگ کردنی لە گرووپ\n\n( `.لادانی ئاگاداری` )\n• بە وەڵامدانەوەی یان نوسینی ناوی بەکارهێنەر لەگەڵ فەرمانەکە بۆ لادانی ئاگاداری\n\nٴ╼──────────────────╾\n\n( `.پین` ) \n• تقوم وەڵامی ئەو نامەیە یان هەر شتێکی تر بدەوە بۆ پین کردنی لە گرووپ\n\n( `.لادانی پین` )\n• بالرد بە وەڵامدانەوەی ئەو نامەی پین کراوە بۆ لادانی لە پین\n\nٴ╼──────────────────╾\n\n( `.بەرزکردنەوەی بەڕێوبەر` ) \n•  وەڵامی ئەو کەسە دەدەیتەوە بۆ بەرزکردنەوەی وەکو بەڕێوبەڕ\n\n( `.داگرتنی بەڕێوبەر` )\n • بە وەڵامدانەوەی ئەو کەسە بۆ داگرتنی لە بەڕێوبەری\n\nٴ╼──────────────────╾ \n\n( `.بەرزکردنەوە` ) \n• بۆ بەرزکردنەوەی بەکارهێنەر لە هەموو گروپەکاندا بە هەموو مۆڵەتەکان بە ناونیشانێکی شاراوەوە\n\n( `.داگرتن` ) \n• بۆ دابەزاندنی کەسەکە لە پلەی بەڕێوبەری لە هەموو گروپەکاندا\n\nٴ╼──────────────────╾\n\n( `.ڕووداوەکان` )\n• بۆ بینینی دوایین نامە سڕاوەکان لە گروپەکە پێویستە بەڕێوەبەر بیت\n\nٴ╼──────────────────╾\n\n@xv7amo"
JMTRD = "**•❒ فەرمانی بەخێرهاتن و وەڵامدانەوە🕷️🖤**\n\n( `.بەخێربێیت + بەخێرهاتنەکەت` ) \n• فەرمانەکە بنووسە لەگەڵ شێوازی بەخێرهاتنەکەت بۆ پێشوازی کردن لە ئەندامە نوێیەکان🦋🤍\n\n( `.سڕینەوەی بەخێرهاتن` ) \n• تەنھا فەرمانەکە بنێرە لەناو گروپەکە بۆ سڕینەوەی بەخێرهاتنەکان🖤🕷️\n\nٴ╼──────────────────╾\n\n( `.بەخێرهاتنەکان` ) \n• فەرمانەکە بنێرە بۆ بینینی بەخێرهاتنی گرووپ\n\n( `.کوژاندنەوە و پێکردنی بەخێرهاتن` )\n• بۆ ناچالاککردنی دوایین بەخێرهاتن کە خستتە ناو گروپەکە یان چالاککردنی🕷️🖤\n\nٴ╼──────────────────╾\n\n( `.زیادکردنی چات + چاتەکەت` ) \n• 🦎🖤بۆ دانانی وەڵامێکی دیاریکراو لە گروپەکە فەرمان و وەڵامەکەت بنوسە\n\n( `.سڕینەوەی چات` ) \n• تەنھا فەرمانەکە بنێرە بۆ سڕینەوەی چاتە زیادکراوەکان\n\nٴ╼──────────────────╾\n\n( `.زیادکراوەکان` ) \n• فەرمانەکە بنێرە لە گرووپ بۆ بینینی چاتە زیادکراوەکان\n\nٴ╼──────────────────╾\n@xv7amo"
JMGR1 = "**•❒ فەرمانی گرووپ🕷️🖤**\n\n( `.شکێنەر` ) \n• نووسینی ئەم فەرمانە تەنھا لەگرووپەکانە بۆ دەرکردنی گشت ئەندامەکان🕷️🖤\n\nٴ╼──────────────────╾\n\n( `.سڕینەوەی قەدەغەکراوەکان` ) \n• نووسینی فەرمانەکە لە گروپەکە بۆ لابردنی هەموو ئەندامەکان\n\n( `.دەرمبکە` ) \n• ئەم فەرمانە بەکاردێت بۆ جێهێشتنی گرووپ🕷️🖤\n\nٴ╼──────────────────╾\n\n( `.قەدەغەکراوەکان` ) \n• بۆ بینینی ئەکاونتە قەدەغەکراوەکان لە گرووپ بۆ سڕینەوەشیان ئەمە بنێرە .سڕینەوەی قەدەغەکراوەکان🕷️🖤\n\n( `.ئەندامەکان` ) \n• ئەم فەرمانە بەکاردێت بۆ بینینی ئەندامەکانی گرووپ🕷️🖤\n\nٴ╼──────────────────╾\n\n( `.بەڕێوبەرەکان` ) \n• ئەم فەرمانە بەکاردێت بۆ بینینی بەڕێوبەرەکانی گرووپ🕷️🖤\n\n( `.بۆتەکان` )\n• ئەم فەرمانە بەکاردێت بۆ بینینی بۆتەکانی گرووپ🕷️🖤\n\nٴ╼──────────────────╾\n@xv7amo"
JMAN = "**•❒  فەرمانی ڕابواردن🕷️🖤**\n\n`.گەمژە`  `.بۆمبەکان`  `.پەیوەندی`   `.کوشتن`    `.خشت`\n\n`.چوارگۆشە`   `.شیرنەمەنی`     `.ئاگر`    `.بارکردن`\n\n`.وابزانم`    `.مرد`    `.بێزار`    `.کاتژمێر`\n\n`.مواح`    `.دڵ`     `.جيم`     `.زەوی`\n\n`.مانگ`      `.مانگەکان`     `.جوان `    `.ئەستێرە`\n\n`.شەشپاڵوەکان`   `.باران `     `.لادان`      `.فیلم`\n\n`.خۆشمەوێی`   `.فڕۆکە`        `.پۆلیس `\n\n`.سیستەمی خۆر`    `.بکوژ`\n\n`.بیرکردنەوە`      `.افعى`         `.پێچانەوە`      `.مایکڕۆ`\n\n`.ڤایرۆس`    `.قیتار`      `.مۆسیقا `\n\n`.وێنەکێشان`   `.دابەزاندن`     `.چوارگۆشە`       `.بازنە`\n\n`.ئەنیم`    `.مرۆڤ`      `.مەیمون`      `.دەست`\n\n`. نزمبوونەوە`        `.دڵی`\n\nٴ╼──────────────────╾\n • هەموو فەرمانەکان بەکاردێت بە کلیك کردن لەسەر فەرمانەکە و کۆپی دەکات و تەنھا دەینێریت🕷️🖤"
JROZT = "**•❒ فەرمانی ئەکاونت🕷️🖤 **\n\n( `.ناوی کات` )\n• ئەم فەرمانە بۆ زیادکردنی ناوی کاتی من، لەلایەن هەرێمێك کە تۆ داتناوە🕷️🖤.\n\n( `.لادانی ناوی کات` )\n• بۆ لادانی ناوی کات و گەڕانەوە بۆ ناوی سروشتی خۆی🕷️🖤.\n\nٴ╼──────────────────╾\n\n( `.بایۆی کات` )\n• ئەم فەرمانە بۆ زیادکردنی بایۆیی کاتی من بە پێی هەرێمێك کە تۆ داتناوە🕷️🖤.\n• بۆ دانانی بایۆی تایبەت بەخۆت🕷️🖤. ( `.جۆری بایۆ`) \n\n( `.لادانی بایۆی کات` )\n• بۆ لادانی بایۆی کات و گەڕانەوەی بۆ سروشتی خۆی🕷️🖤.\nٴ\n╼──────────────────╾\n\n(  `.وێنەی کات`  )\n• وێنەی ئەکاونتی تایبەتی تۆ کات نیشان دەدات و هەموو خولەکێك دەگۆڕێت بۆ زانیاری زیاتر لەسەر ئەم بابەتە بنێرە '.ڤار کاتی🕷️🖤.`\n\n(  `.لادانی وێنەی کات` )\n• بۆ لادانی وێنەی کات‌🕷️🖤.\nٴ\n╼──────────────────╾\n\n( `.دۆخی ناو <ناوت>`  )\n• بۆ گۆڕینی ناوی ئەکاونتی تایبەتی خۆت لەسەر تەلگرام، فەرمانەکە بنووسە بە ناوی ئەکاونتەکەوە🕷️🖤.\n\n(  `.دۆخی بایۆ <بایۆ>` )\n• بۆ گۆڕینی پرۆفایلەکەت لەسەر تەلگرام، فەرمانەکە بنووسە لەگەڵ بایۆکەت🕷️🖤.\n\n(  `.سڕینەوەی وێنە`  )\n•بۆ سڕینەوەی وێنەکانی ئەکاونتەکەت بە نووسینی فەرمان بۆ سڕینەوەی وێنەیەك🕷️🖤.\n\n( `.دۆخی وێنە <بەوەڵامدانەوەی>` )\n•بۆ گۆڕینی وێنەی ئەکاونتی تایبەتی خۆت لەسەر تەلگرام، فەرمانەکە بنوسە بە وەڵامدانەوەی وێنەکە🕷️🖤.\n\nٴ╼──────────────────╾\n@xv7amo"
TKPRZ = "**•❒ فەرمانی پاککردنەوە و دووبارەکردنەوە🕷️🖤**\n\n( `.كرر  <عدد التكرار> <بالرد>` )\n• يقوم بتكرار النصوص والوسائط بالرد على الرسالة او الصورة  بامر كرر مع عدد التكرار\n\n( `.تكرار الملصق <بالرد عل ملصق>` ) \n• بالرد على الملصق ليقوم باستخراج جميع ملصقات الحزمه وارسالها\n\n( `.مكرر  < وقت بالثواني><عدد><بالرد>` )\n• بالرد على نص او صورة او اي شي يقوم بالتكرار  مع وقت معين .\n\n( `.ضع تكرار <العدد>` )\n• لمنع التكرار بالمجموعة الخاصة بك بالعدد الذي وضعته للعودة للوضع الطبيعي ضع 999999.\n\n╼──────────────────╾\n\n( `.سبام < كلمـة >` )\n• يقوم بتفصيخ احرف الكلمه وارسالها جربه بنفسك\n\n( `.وسبام < كلـمة >`)\n• كتابة الامر مع نص معين يقوم بتفصيخ الجمله كلمه كلمه وارسالها\n\nٴ╼──────────────────╾\n\n( `.تنظيف + عدد الرسائل` )\n• يقوم بحذف الرسائل اكتب الامر وعدد معين من الرسائل سيقوم بحذفها \n\nٴ╼──────────────────╾\n\n( `.مسح  <بالرد على النص>` )\n• فقط اكتب الامر بالرد على الرسالة ليقوم بحذفها \n\n( `.حذف رسائلي` )\n• اكتب الامر في اي مكان وسيقوم بحذف جميع رسائلك في الدردشه حتى لو لم يكن لديك صلاحيات \n\nٴ╼──────────────────╾\n\n@xv7amo"
GRTSTI = "**•❒ فەرمانی ستیکەرەکان و هەمەجۆر🕷️🖤**\n\n( .ملصق )\n• بالرد على الملصق لأخذه و عمل حزمه خاصة بك و اضافته بها\n\n( .حزمة )\n• بالرد على الملصق لنسخ الحزمة كاملة بداخل حزمة ملصقاتك الخاصة\n\n(.معلومات_الملصق )\n• بالرد على الملصق لعرض معلومات الحزمة\n\nٴ╼──────────────────╾\n\n( .صور +  عدد الصور + نص )\n• للحصول على صور من متصفح كوكل بكتابة الامر وعدد الصور الحد 10 واسم النص\n\n( .موقع + المكان )\n• للحصول على مكان في الخريطه و ارساله لك\n\n( `.صورة` )\n• بالرد على الشخص للحصول على صورة حسابه الشخصية.\n\n( `.صورة كلها` )\n• للرد على الشخص للحصول على صور حسابه الشخصية كلها.\n\n( `.سرعة الانترنت` )\n• ارسل الامر لقياس سرعة الانترنت\n\n( `.حساب` )\nكتابة الامر مع معادلة رياضية و سيقوم بحلها و ارسالها لك\n\nٴ╼──────────────────╾\n@xv7amo"
HERP = "**•❒ فەرمانی زیادە🕷️🖤**\n\n( `.جلب الصورة` ) \n• بالرد على صورة ذاتية التدمير لتحميلها وارسالها لك في الرسائل المحفوظة بسرية تامة\n\n(  .الرابط  ) \n• اكتب الامر في المجموعة لعرض رابط المجموعة يجب ان تكون مشرف\n\n(  `.معنى <الاسم>`  ) \n• لعرض معنى اسمك وارسال رسالة مع وصف للاسم\n\n(  `.قراءة < بالرد على ملف>`  ) \n• بالرد على ملف لعرض ما في داخل الملف ونسخه وارساله  لك\n\n(  `.حالتي` )\n• لعرض حاله حسابك اذا كان محظور او لا في التلي\n\n( `.ايميل وهمي` ) \n\n• لصنع ايميل وهمي وارساله لك\n\n(  `.حاسبة` ) \n• لعرض حاسبة علمية يجب ان تفعل وضع الانلاين\n\n( `.تاريخ` )\n• بالرد على الشخص او كتابة معرفه مع الامر لعرض سجل اسماء حسابه.\n\n( `.کات` )\n• لعرض الوقت الحالي على شكل ملصق\n\n( `.کاتی` )\n• لعرض الوقت الحالي على شكل كتابة\n\n( `.مؤقت <الوقت> < النص> ` )\n• يقوم بإرسال رسالة مؤقتة و حذفها بعد وقت معين\n\n( `.كورونا < الدولة>` )\n• للحصول على احصائيات فايروس كورونا اكتب الامر مع اسم الدولة بالانكليزي\n\n( `.صلاة` < اسم محافظة> )\n• اكتب الامر مع اسم محافظتك باللغه الانكليزية للحصول على اوقات الصلاة\n\nٴ╼──────────────────╾\n@xv7amo"
CLORN = "**•❒ فەرمانی تەقلید و کۆپی🕷️🖤**\n\n( `.کۆپی` ) \n• بالرد على الشخص لنسخ حسابه بالكامل من صورة واسم وبايو  \n\n( `.اعادة` ) \n• لارجاع الحساب الى وضعه الطبيعي لما كان سابقا\n\nٴ╼──────────────────╾\n\n( `.لاسایی کردنەوە` ) \n• بالرد على الشخص لتقليد جميع رسائله في الدردشه \n\n( `.لادانی لاسای کردنەوە` ) \n• بالرد على الشخص لايقاف التقليد\n\n( `.المقلدهم` ) \n• لاظهـار قائمه الاشخاص الذي فعـلت عليهم امر التقليد ولمسحهم ارسل  ( `.مسح المقلدهم` ) \n\nٴ╼──────────────────╾\n\n( `.تاك` + معرف + نص ) \n\n• لعمل تاك لشخص في الكروب و وضع التاك في النص \n• مثـال | .تاك @Jepthon  ههلا \n\n( `.للكل + نص` ) \n• لعمل تاك للكل مع النص اكتب الامر مع النص وارسله فقط\n\n( `.ابلاغ` )\n• بالرد على الشخص لعمل ابلاغ لمشرفين المجموعة\n\nٴ╼──────────────────╾\n\n@xv7amo"
T7SHIZ = "•❒ داواکاری خۆشی بۆ ڕابواردن🕷️🖤\n\n`.بمژا`        .ڕسوایی`      `.بڕین`    `.هاوسەرگیری`\n\n`.تەڵاق`    `.رفع مطي`    `.رفع زوجي`\n\n`.ژنەکەت بەرزکەوە`      `.بەرزکردنەوەی تاج`   `.ڕێژەی ئافرەت`\n\n`.ڕێژەی گەمژەیی`   `.ڕێژەی خۆشەویستی`  `.مەیمون`\n\n`.وێنە`   `.دڵم`\n\n`.نسبة الكذب`      `.نسبة الشذوذ`   `.نسبة الدياثه`\n\n`.نسبة الغباء`    `.نسبة الحب`   `.نسبة الجمال`\n\n`.رفع زاحف`     `.نسبة الخيانه`\n\n`.رفع صاك`      `.رفع فرخ`   `.رفع كحبة`\n\n`.رفع ايجة`   `.بەخێوکردنی مانگایەک`   `.رفع حاته`\n\n`.رفع كواد`     `.رفع زبال`\n\n`.رفع مميز`      `.رفع مجنب`   `.رفع ديوث`\n\n`.پارەکەت کۆبکەوە`    `.رفع منشئ`   `.رفع ادمن`\n\n`.محمد`     `. هەڵگرتنی پیسی`\n\nٴ╼──────────────────╾\n\nهەموو ئەم فەرمانانە بە وەڵامدانەوەی نامەی کەسەکە ئەنجام ئەدرێت"
ROZ_IC = "https://telegra.ph/file/3851323764f1629e16ce8.jpg"
ROE = "** ئەمە لیستی فەرمانەکانی سەرچاوەی بۆتی زیرەکە🕷️🖤. **"
