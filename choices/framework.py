from enum import Enum


# feature for the future if the modals allow to make a selection menu.
class Framework(Enum):
    # FRONT END
    REACT = "React"
    VUE_JS = "VueJS"
    VITE = "ViteJS"
    SVELTE = "Svelte"
    ANGULAR = "Angular"
    TAILWIND = "Tailwind css"
    BOOTSTRAP = "Bootstrap"
    CORDOVA = "Cordova"
    NEXT_JS = "Next.js"
    METEOR = "Meteor"

    # BACK END
    NODEJS = "Node.js"
    NUXT_JS = "Nuxt.js"
    LARAVEL = "Laravel"
    SYMFONY = "Symfony"
    SPRING = "Spring"
    SPRING_BOOT = "Spring boot"
    ASP_NET = "ASP.NET"
    NET = ".NET"
    NEST_JS = "Nest.js"
    EXPRESS_JS = "Express.js"
    RUBY_ON_RAILS = "Ruby on Rails"
    VAPOR = "VAPOR"
    GIN = "GIN"
    KTOR = "KTOR"
    DJANGO = "Django"
    FLASK = "Flask"
    GRAILS = "Grails"
    KOA_JS = "Koa.js"
    REASON = "Reason"
    YII_TWO = "Yii2"
    NETTE = "Nette"

    # GAME DEV
    GODOT = "Godot"
    MONOGAME = "Monogame"
    UNREAL = "Unreal engine"
    UNITY = "Unity"
    RPG_ENGINE = "RPG engine"
    COCOS_CREATOR = "Cocos Creator"
    CONSTRUCT = "Construct"
    PROCESSING = "Processing"
    GAMEMAKER = "Game maker"

    # MOBILE
    REACT_NATIVE = "React Native"
    FLUTTER = "Flutter"
    XAMARIN = "Xamarin"
    MAUI = "Maui"
    AVALONIA = "Avalonia"
    NATIVE_IOS = "Native ios"
    COCOA = "Cocoa"
    SWIFT_UI = "Swift UI"

    # CMS
    STRAPI_JS = "Strapi.js"
    WORDPRESS = "Wordpress"
    PRESTASHOP = "Prestashop"
    DRUPAL = "Drupal"
    JOOMLA = "JOOMLA"
    SHOPIFY = "SHOPIFY"

    # BDD
    HIBERNATE = "Hibernate"

    # JAVA
    HADOOP = "Hadoop"
    SWING = "Swing"
    JAKARTA = "Jakarta"
    QUARKUS = "Quarkus"
    COMPOSE = "Compose"
    MICRONAUT = "Micronaut"
    JAVA_FX = "Java fx"
    PLAY = "Play"
    JAVA_EE = "Java EE"
    JAVA_SE = "Java SE"
    JAVA_ME = "Java ME"

    # Python
    FAST_API = "Fast api"
    PYGAME = "Pygame"
    PYTORCH = "Pytorch"
    TENSORFLOW = "TensorFlow"
    KERAS = "Keras"
    PANDAS = "Pandas"
    PYRAMID = "Pyramid"

    # C/CPP
    SDL = "SDL"
    CUDA = "Cuda"
    QT = "QT"
    WX_WIDGETS = "WX_Widgets"
    DEARLMGUI = "DearlMGUI"

    # OTHER
    EMBEDDED = "Embedded"
    SMT_CUBE = "SMTCude"

    # R
    TAURI = "Tauri"
