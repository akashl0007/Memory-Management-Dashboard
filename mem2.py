import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
import psutil


class MemoryUsageApp(App):

    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.filter_spinner = Spinner(text="All Processes", values=[
                                      "All Processes"] + sorted(list(set(p[0] for p in self.collect_memory_data()))))
        self.filter_spinner.bind(text=self.on_filter_change)
        self.layout.add_widget(self.filter_spinner)

        self.group_toggle = ToggleButton(
            text="Group by Process", state="normal")
        self.group_toggle.bind(state=self.on_group_toggle)
        self.layout.add_widget(self.group_toggle)

        self.sort_button = Button(
            text="Sort by Memory Usage", on_release=self.sort_by_memory)
        self.layout.add_widget(self.sort_button)

        self.process_labels = [Label(text=self.format_process_label(
            process_name, memory_usage)) for process_name, memory_usage in self.collect_memory_data()]
        self.refresh_ui()

        return self.layout

    def collect_memory_data(self):
        memory_data = []
        for process in psutil.process_iter(['pid', 'name', 'memory_info']):
            process_info = process.info
            process_name = process_info['name']
            memory_usage = process_info['memory_info'].rss
            memory_data.append((process_name, memory_usage))
        return memory_data

    def format_process_label(self, process_name, memory_usage):
        return f"Process: {process_name}\nMemory Usage: {memory_usage} bytes"

    def refresh_ui(self):
        self.layout.clear_widgets()
        self.layout.add_widget(self.filter_spinner)
        self.layout.add_widget(self.group_toggle)
        self.layout.add_widget(self.sort_button)

        filtered_data = self.collect_memory_data() if self.filter_spinner.text == "All Processes" else \
            [(name, mem) for name, mem in self.collect_memory_data()
             if name == self.filter_spinner.text]

        if self.group_toggle.state == "down":
            grouped_data = {}
            for name, mem in filtered_data:
                if name not in grouped_data:
                    grouped_data[name] = 0
                grouped_data[name] += mem
            filtered_data = [(name, mem) for name, mem in grouped_data.items()]

        if hasattr(self, 'sorted_by_memory') and self.sorted_by_memory:
            filtered_data.sort(key=lambda x: x[1], reverse=True)

        for process_name, memory_usage in filtered_data:
            label = Label(text=self.format_process_label(
                process_name, memory_usage))
            self.layout.add_widget(label)

    def on_filter_change(self, instance, text):
        self.refresh_ui()

    def on_group_toggle(self, instance, state):
        self.refresh_ui()

    def sort_by_memory(self, instance):
        self.sorted_by_memory = not hasattr(
            self, 'sorted_by_memory') or not self.sorted_by_memory
        self.refresh_ui()


if __name__ == '__main__':
    MemoryUsageApp().run()
