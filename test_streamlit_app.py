import runpy
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import patch


class StreamlitEntrypointTest(unittest.TestCase):
    def test_entrypoint_renders_the_complete_bundled_portal(self):
        calls = {}
        entrypoint = Path(__file__).with_name("streamlit_app.py")
        self.assertTrue(entrypoint.exists(), "Streamlit entrypoint is missing")

        streamlit = types.ModuleType("streamlit")
        streamlit.set_page_config = lambda **kwargs: calls.setdefault("config", kwargs)

        components = types.ModuleType("streamlit.components.v1")
        components.html = lambda body, **kwargs: calls.setdefault(
            "render", (body, kwargs)
        )

        modules = {
            "streamlit": streamlit,
            "streamlit.components": types.ModuleType("streamlit.components"),
            "streamlit.components.v1": components,
        }

        with patch.dict(sys.modules, modules):
            runpy.run_path(entrypoint)

        expected_html = Path(__file__).with_name("index.html").read_text(
            encoding="utf-8"
        )
        rendered_html, render_options = calls["render"]

        self.assertEqual(rendered_html, expected_html)
        self.assertTrue(render_options["scrolling"])
        self.assertGreaterEqual(render_options["height"], 1200)
        self.assertEqual(
            calls["config"]["page_title"], "微康核心菌株科研成果智查助手"
        )


if __name__ == "__main__":
    unittest.main()
