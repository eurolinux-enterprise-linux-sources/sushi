
/* Generated data (by glib-mkenums) */

#include "sushi-enum-types.h"
/* enumerations from "libsushi/sushi-sound-player.h" */
#include "libsushi/sushi-sound-player.h"
GType
sushi_sound_player_state_get_type(void) {
  static GType enum_type_id = 0;
  if (G_UNLIKELY (!enum_type_id))
    {
      static const GEnumValue values[] = {
        { SUSHI_SOUND_PLAYER_STATE_UNKNOWN, "SUSHI_SOUND_PLAYER_STATE_UNKNOWN", "unknown" },
        { SUSHI_SOUND_PLAYER_STATE_IDLE, "SUSHI_SOUND_PLAYER_STATE_IDLE", "idle" },
        { SUSHI_SOUND_PLAYER_STATE_PLAYING, "SUSHI_SOUND_PLAYER_STATE_PLAYING", "playing" },
        { SUSHI_SOUND_PLAYER_STATE_DONE, "SUSHI_SOUND_PLAYER_STATE_DONE", "done" },
        { SUSHI_SOUND_PLAYER_STATE_ERROR, "SUSHI_SOUND_PLAYER_STATE_ERROR", "error" },
        { 0, NULL, NULL }
      };
      enum_type_id = g_enum_register_static("SushiSoundPlayerState", values);
    }
  return enum_type_id;
}

/* Generated data ends here */

