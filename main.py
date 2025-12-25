from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QLabel
)
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt
from deep_translator import GoogleTranslator

class TranslatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🌐 مترجم أمازيغي - عربي")
        self.resize(800, 600)
        self.setStyleSheet("background-color: #1e1e2f; color: #ffffff;")

        # خطوط جذابة
        self.font_title = QFont("Arial", 24, QFont.Bold)
        self.font_subtitle = QFont("Arial", 14)
        self.font_text = QFont("Arial", 16)

        # عنوان رئيسي
        self.title_label = QLabel("🌐 مترجم أمازيغي - عربي")
        self.title_label.setFont(self.font_title)
        self.title_label.setAlignment(Qt.AlignCenter)

        # عنوان فرعي
        self.subtitle_label = QLabel("✨ ترجمة مجانية 100% - بدون قيود")
        self.subtitle_label.setFont(self.font_subtitle)
        self.subtitle_label.setStyleSheet("color: #10b981;")
        self.subtitle_label.setAlignment(Qt.AlignCenter)

        # مربعات النصوص
        self.input_text = QTextEdit()
        self.input_text.setFont(self.font_text)
        self.input_text.setPlaceholderText("🔵 أدخل النص الأمازيغي هنا...")
        self.input_text.setStyleSheet(
            "background-color: #2e2e3f; border: 2px solid #3b82f6; border-radius: 10px; color: #ffffff;"
        )

        self.output_text = QTextEdit()
        self.output_text.setFont(self.font_text)
        self.output_text.setReadOnly(True)
        self.output_text.setStyleSheet(
            "background-color: #2e2e3f; border: 2px solid #8b5cf6; border-radius: 10px; color: #ffffff;"
        )

        # زر الترجمة
        self.translate_button = QPushButton("⚡ ترجم الآن")
        self.translate_button.setFont(QFont("Arial", 16, QFont.Bold))
        self.translate_button.setStyleSheet(
            "background-color: #3b82f6; color: white; border-radius: 10px; height: 40px;"
        )
        self.translate_button.clicked.connect(self.translate_text)

        # زر النسخ للنص العربي
        self.copy_button = QPushButton("📋 نسخ الترجمة")
        self.copy_button.setFont(QFont("Arial", 14))
        self.copy_button.setStyleSheet(
            "background-color: #8b5cf6; color: white; border-radius: 10px; height: 35px;"
        )
        self.copy_button.clicked.connect(self.copy_translation)

        # تخطيط الأزرار
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.translate_button)
        button_layout.addWidget(self.copy_button)

        # التخطيط العام
        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.subtitle_label)
        layout.addSpacing(10)
        layout.addWidget(self.input_text)
        layout.addLayout(button_layout)
        layout.addWidget(self.output_text)

        self.setLayout(layout)

    def translate_text(self):
        text = self.input_text.toPlainText().strip()
        if not text:
            self.output_text.setPlainText("⚠️ الرجاء إدخال نص للترجمة")
            return
        try:
            translator = GoogleTranslator(source='auto', target='ar')
            translation = translator.translate(text)
            self.output_text.setPlainText(translation)
        except Exception as e:
            self.output_text.setPlainText(f"❌ خطأ في الترجمة: {e}")

    def copy_translation(self):
        text = self.output_text.toPlainText()
        if text:
            QApplication.clipboard().setText(text)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = TranslatorApp()
    window.show()
    sys.exit(app.exec_())
