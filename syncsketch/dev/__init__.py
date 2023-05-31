from typing import Type

from ayon_server.addons import BaseServerAddon, AddonLibrary
from ayon_server.lib.postgres import Postgres

from .settings import SyncsketchSettings, DEFAULT_VALUES


class SyncsketchAddon(BaseServerAddon):
    name = "syncsketch"
    title = "SyncSketch"
    version = "1.0.0"
    settings_model: Type[SyncsketchSettings] = SyncsketchSettings

    async def get_default_settings(self):
        settings_model_cls = self.get_settings_model()
        return settings_model_cls(**DEFAULT_VALUES)

    async def setup(self):
        need_restart = await self.create_applications_attribute()
        if need_restart:
            self.request_server_restart()

    async def create_applications_attribute(self) -> bool:
        """Make sure there are required attributes which ftrack addon needs.

        Returns:
            bool: 'True' if an attribute was created or updated.
        """
        query = "SELECT name, position, scope, data from public.attributes"

        id_attrib_name = "syncsketchId"

        id_attribute_data = {
            "type": "string",
            "title": "SyncSketch ID",
            "inherit": False
        }

        id_scope = ["project", "version"]

        id_match_position = None
        id_matches = False

        position = 1

        async for row in Postgres.iterate(query):
            position += 1
            if row["name"] == id_attrib_name:
                # Check if scope is matching ftrack addon requirements
                if (set(row["scope"]) == set(id_scope)):
                    id_matches = True
                id_match_position = row["position"]

        if id_matches:
            return False

        postgres_query = "\n".join((
            "INSERT INTO public.attributes",
            "    (name, position, scope, data)",
            "VALUES",
            "    ($1, $2, $3, $4)",
            "ON CONFLICT (name)",
            "DO UPDATE SET",
            "    scope = $3,",
            "    data = $4",
        ))
        if not id_matches:
            # Reuse position from found attribute
            if id_match_position is None:
                id_match_position = position
                position += 1

            await Postgres.execute(
                postgres_query,
                id_attrib_name,
                id_match_position,
                id_scope,
                id_attribute_data,
            )

        return True
