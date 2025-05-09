from bird_sound_player import play_bird_defense

if __name__ == "__main__":
    print("\n 새 퇴치 사운드 단일 테스트 시작")

    # 테스트 대상
    test_bird = "참새"  # "까마귀", "참새", "멧비둘기", "까치" 등으로 바꿔가며 테스트 가능

    print(f"\n '{test_bird}' 퇴치 테스트 중...\n")
    play_bird_defense(test_bird)
