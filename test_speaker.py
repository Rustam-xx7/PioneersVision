"""
Test script to verify speaker.py is working properly
"""
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from func_root.speech.speaker import speak

def test_speaker_basic():
    """Test basic speaker functionality"""
    print("=== Testing Speaker Module ===\n")
    
    try:
        # Test 1: Basic English text
        print("Test 1: Speaking basic English text...")
        speak("Hello, this is a test")
        print("✓ Test 1 passed\n")
        
    except Exception as e:
        print(f"✗ Test 1 failed: {e}\n")
    
    try:
        # Test 2: Read from recognized_text.txt
        print("Test 2: Reading from recognized_text.txt...")
        text_file = "recognized_text.txt"
        
        if os.path.exists(text_file):
            with open(text_file, "r", encoding="utf-8") as f:
                content = f.read().strip()
            
            print(f"  File content: '{content}'")
            
            if content:
                print(f"  Speaking content...")
                speak(content)
                print("✓ Test 2 passed\n")
            else:
                print("  Warning: File is empty\n")
        else:
            print(f"  Warning: {text_file} not found\n")
            
    except Exception as e:
        print(f"✗ Test 2 failed: {e}\n")
    
    try:
        # Test 3: Test with different languages (if Azure is enabled)
        print("Test 3: Testing with Hindi...")
        speak("नमस्ते", language="hi-IN", gender="female")
        print("✓ Test 3 passed\n")
        
    except Exception as e:
        print(f"✗ Test 3 failed: {e}\n")
    
    try:
        # Test 4: Test with empty text (should fail validation)
        print("Test 4: Testing with empty text (should fail)...")
        speak("")
        print("✗ Test 4 should have failed but didn't\n")
        
    except Exception as e:
        print(f"✓ Test 4 passed (correctly rejected empty text): {e}\n")
    
    print("=== Test Complete ===")

if __name__ == "__main__":
    test_speaker_basic()
