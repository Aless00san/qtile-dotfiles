# ~/.config/qtile/config.py
import os

import subprocess

import libqtile.resources  # type: ignore
from libqtile import bar, layout, widget  # type: ignore
from libqtile.config import Click, Drag, Group, Key, Match, Screen  # type: ignore
from libqtile import hook  # type: ignore
from libqtile.lazy import lazy  # type: ignore

import os
from libqtile import hook


@hook.subscribe.startup
def start_compositor():
    """Start Picom if not already running."""
    try:
        subprocess.check_output(["pgrep", "-x", "picom"])
    except subprocess.CalledProcessError:
        subprocess.Popen([
            "picom",
            "--experimental-backends",
            "--config",
            os.path.expanduser("~/.config/picom/picom.conf")
        ])


def check_bluetooth_status():
    try:
        result = subprocess.run(
            ['bluetoothctl', 'show'],
            capture_output=True,
            text=True,
            timeout=1
        )
        if 'Powered: yes' in result.stdout:
            return 'ON'
        else:
            return 'OFF'
    except:
        return 'N/A'

def left_arrow(bg_color, fg_color):
    return widget.TextBox(
        text='\uE0B2',
        padding=0,
        fontsize=40,
        background=bg_color,
        foreground=fg_color
    )

# -------------------------
# MOD KEY & TERMINAL
# -------------------------
mod = "mod4"
terminal = "alacritty"  # your preferred terminal

# -------------------------
# KEYBINDINGS
# -------------------------
keys = [
    # Move focus
    Key([mod], "h", lazy.layout.left(), desc="Move focus left"),  # type: ignore
    Key([mod], "l", lazy.layout.right(), desc="Move focus right"),  # type: ignore
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),  # type: ignore
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),  # type: ignore
    Key([mod, "shift"], "space", lazy.layout.next(), desc="Move focus to next window"),  # type: ignore

    # Move windows
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window left"),  # type: ignore
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window right"),  # type: ignore
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),  # type: ignore
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),  # type: ignore

    # Grow/shrink windows
    # Resize windows
    Key([mod, "control"], "h", lazy.layout.shrink(), desc="Shrink master width"),
    Key([mod, "control"], "l", lazy.layout.grow(), desc="Grow master width"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset window sizes"),  # type: ignore

    # Toggle split layout
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle split layout"),  # type: ignore

    # Launch terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),  # type: ignore

    Key([mod], "space", lazy.spawn("rofi -show drun"), desc="Launch applications"),

    # Switch layouts
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle layouts"),
    

    # Close window
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),  # type: ignore

    # Other
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),  # type: ignore    
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload Qtile config"),  # type: ignore
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),  # type: ignore
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command via prompt"),  # type: ignore

    # Take screenshoot
    Key(["mod4", "control"], "Print", lazy.spawn("flameshot full -c")),
    
    #Lock screen
    Key([mod], "l", lazy.spawn("bash .config/qtile/lock.sh")),   


    # Fn keys
    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 10")),
    

    # Volume (for PipeWire via wpctl)
    Key([], "XF86AudioRaiseVolume", lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-")),
    Key([], "XF86AudioMute", lazy.spawn("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle")),

]

# -------------------------
# GROUPS
# -------------------------

groups = [
        Group("1", label="フ"),  
        Group("2", label="リ"),  
        Group("3", label="ク"),
        Group("4", label="リ")  
    ]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc=f"Switch to group {i.name}"),  # type: ignore
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc=f"Move focused window to group {i.name}"),  # type: ignore
    ])

# -------------------------
# LAYOUTS
# -------------------------
layouts = [
   layout.MonadTall(
            margin=10,
            border_width=0,
            border_focus="#88C0D0",
            border_normal="#4C566A",
            ratio=0.6
        ),
    layout.Max(),  # type: ignore
]

# -------------------------
# WIDGETS
# -------------------------
widget_defaults = dict(
    font="0xProto Nerd Font",
    fontsize=20,
    padding=5,
    background="#00000080",  # 50% opacity black
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper="~/.local/share/backgrounds/2025-07-14-17-17-16-F2rCF4e.jpeg",
        wallpaper_mode='fill',
        bottom=bar.Bar(
            [
                widget.TextBox(
                                    text="", 
                                    fontsize=24,
                                    padding=12,
                                    foreground="#DEDEE0",
                                ),
                widget.CurrentLayout(
                    fontsize=18
                ),  # type: ignore
                widget.GroupBox(
                                    highlight_method="block",
                                    this_current_screen_border="#88C0D0",
                                    this_screen_border="#5E81AC",
                                    other_current_screen_border="#4C566A",
                                    other_screen_border="#4C566A",
                                    active="#ECEFF4",
                                    inactive="#4C566A",
                                    rounded=True,
                                    disable_drag=True,
                                    font="0xProto Nerd Font Mono",
                                    fontsize=16,
                                ), # type: ignore
                widget.Prompt(),  # type: ignore
                widget.Spacer(),
                widget.Clock(
                format="%d/%m %a %I:%M",
                fontsize=24,),  # type: ignore
                widget.Spacer(),
                left_arrow("#00000080", "#519872"),
                widget.Battery(
                    format="{char} {percent:2.0%}",
                    charge_char="",  
                    discharge_char="",
                    empty_char="",
                    full_char="",
                    full_short_text=" 100%",
                    update_interval=30,  # seconds
                    background="#519872",
                    show_short_text=True,
                ),
                left_arrow("#519872", "#22333B"),
                widget.CPU(
                    format=" {load_percent}%",
                    update_interval=2,
                    fontsize=18,
                    foreground="#FFFFFF",
                    background="#22333B"
                ),
                left_arrow("#22333B", "#9297C4"),
                widget.Memory(
                    format=" {MemPercent}%",  # Shows memory usage in %
                    measure_mem="G",             # Optional: measure in GB
                    update_interval=2,           # seconds
                    fontsize=18,
                    background="#9297C4"
                ),
                left_arrow("#9297C4", "#3C91E6"),
                widget.GenPollText(
                    func=lambda: check_bluetooth_status(),
                    update_interval=5,
                    fmt='󰂯:{}',
                    background="#3C91E6",
                    mouse_callbacks={
                        'Button1': lazy.spawn('blueman-applet'),  # Left click
                        'Button3': lazy.spawn('pkill blueman'),                    }
                ),
                left_arrow("#3C91E6", "#593678"),
                 widget.Volume(
                                    fmt='Vol: {}',
                                    step=5,  # Volume change step (5%)
                                    mouse_callbacks={
                                        'Button3': lazy.spawn('pavucontrol')  # Right-click opens pavucontrol
                                    },
                                    background="#593678",
                                ),
                left_arrow("#593678", "#ff0000"),
                widget.QuickExit(
                    default_text='[X]',
                    countdown_format='[{}]',
                    fontsize=22,
                    background="#ff0000"
                ),  # type: ignore

            ],
            36,
        ),
        top = bar.Bar([
            widget.Spacer(),
            widget.Systray(
            ),
            widget.Spacer()
        ], 20)
        ,
    ),
    
]

# -------------------------
# MOUSE
# -------------------------
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),  # type: ignore
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),  # type: ignore
    Click([mod], "Button2", lazy.window.bring_to_front()),  # type: ignore
]

# -------------------------
# FLOATING LAYOUTS
# -------------------------
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,  # type: ignore
        Match(title="pinentry"),  # type: ignore
        Match(wm_class="ssh-askpass"),  # type: ignore
        Match(wm_class="floating_term"),  # custom floating terminal
    ]
)


# -------------------------
# OTHER SETTINGS
# -------------------------
auto_fullscreen = True
focus_on_window_activation = "smart"
bring_front_click = False
cursor_warp = False


# LG3D removed
# wmname = "LG3D"

subprocess.call([os.path.expanduser("~/.config/qtile/autostart.sh")])
