import React, { useEffect, useState } from 'react';

const ImageSection = () => {
  const [latestImage, setLatestImage] = useState(null);
  const [analyzedImage, setAnalyzedImage] = useState(null);
  const [latestAudio, setLatestAudio] = useState(null);
  const [analyzedAudio, setAnalyzedAudio] = useState(null);
  const [predictionText, setPredictionText] = useState("");

  useEffect(() => {
    const fetchPrediction = async (filename) => {
      const txtName = filename.replace(".jpg", ".txt");
      try {
        const res = await fetch(`http://220.149.235.221:4000/save_bird_class/${txtName}`);
        // const res = await fetch(`http://220.149.235.221:4000/images_result/${txtName}`);

        const text = await res.text();
    
        // 응답이 HTML 형식(에러 페이지)이면 무시
        if (text.startsWith('<!doctype html>')) {
          console.warn("❗ 유효하지 않은 예측 결과 (404 또는 HTML 에러 페이지)");
          setPredictionText("");  // 예측 텍스트 초기화
        } else {
          setPredictionText(text.trim());
        }
      } catch (err) {
        console.error("❌ 예측 결과 불러오기 실패:", err);
        setPredictionText("");
      }
    };

    const fetchAssets = async () => {
      try {
        // 이미지
        const imageRes = await fetch('http://220.149.235.221:4000/api/images');
        const imageList = await imageRes.json();
        const latestImg = imageList
          .filter(name => name.startsWith('frame_') && name.endsWith('.jpg'))
          .sort((a, b) => parseInt(b.match(/frame_(\d+)/)?.[1] || 0) - parseInt(a.match(/frame_(\d+)/)?.[1] || 0))[0];
        if (latestImg) {
          setLatestImage(`http://220.149.235.221:4000/images/${latestImg}`);
          await fetchPrediction(latestImg);
        } else {
          setLatestImage(null);
          setPredictionText("");
        }

        // 분석 이미지
        const resultRes = await fetch('http://220.149.235.221:4000/api/images_result');
        const resultList = await resultRes.json();
        const latestResult = resultList
          .filter(name => name.startsWith('frame_result_') && name.endsWith('.jpg'))
          .sort((a, b) => parseInt(b.match(/frame_result_(\d+)/)?.[1] || 0) - parseInt(a.match(/frame_result_(\d+)/)?.[1] || 0))[0];
        // setAnalyzedImage(latestResult ? `http://220.149.235.221:4000/images_result/${latestResult}` : null);
        if (latestResult) {
          setAnalyzedImage(`http://220.149.235.221:4000/images_result/${latestResult}`);
          await fetchPrediction(latestResult); // 추가된 부분
        } else {
          setAnalyzedImage(null);
        }

        try {
        // 오디오
        const audioRes = await fetch('http://220.149.235.221:4000/api/sounds');
        const audioList = await audioRes.json();
        const original = audioList
          .filter(name => !name.includes('_result'))
          .sort((a, b) => parseInt(b.match(/(\d+)/)?.[1] || 0) - parseInt(a.match(/(\d+)/)?.[1] || 0))[0];
        /* const analyzed = original?.replace(/\.(wav|mp3)$/, '_result.$1'); */
        const analyzed = original?.replace(/\.(wav|mp3)$/, '.json');
        setLatestAudio(original ? `http://220.149.235.221:4000/sounds/${original}` : null);
        /* setAnalyzedAudio(analyzed ? `http://220.149.235.221:4000/sounds/${analyzed}` : null); */
        const jsonRes = await fetch(`http://220.149.235.221:4000/sounds/${analyzed}`);
        if (!jsonRes.ok) throw new Error(`JSON 로드 실패: ${jsonRes.status}`);
        const jsonData = await jsonRes.json();

        // 4) JSON의 "name" 키 값을 setAnalyzedAudio에 설정
        const nameValue = jsonData.name;
        setAnalyzedAudio(nameValue ?? null);
        } catch (err) {
          console.error('❌ 처리 중 오류 발생:', err);
          setAnalyzedAudio(null);
        }


      } catch (err) {
        console.error("❌ 전체 리소스 불러오기 실패:", err);
        setLatestImage(null);
        setAnalyzedImage(null);
        setLatestAudio(null);
        setAnalyzedAudio(null);
        setPredictionText("");
      }
    };

    fetchAssets();
    const interval = setInterval(fetchAssets, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="p-8 grid grid-rows-1 gap-5">
      {/* 이미지 영역 */}
      <div className="grid grid-cols-2 gap-6">
        <div>
          <div className="text-center font-bold text-lg mb-3">최근에 찍힌 사진</div>
          <div className="border border-black h-72 flex items-center justify-center">
            {latestImage ? (
              <img src={latestImage} alt="최근 이미지" className="max-h-full object-contain" />
            ) : (
              <span className="text-gray-500">이미지를 불러오는 중...</span>
            )}
          </div>
        </div>
        <div>
          <div className="text-center font-bold text-lg mb-3">AI가 분석한 사진</div>
          <div className="border border-black h-72 flex items-center justify-center">
            {analyzedImage ? (
              <img src={analyzedImage} alt="AI 분석 이미지" className="max-h-full object-contain" />
            ) : (
              <span className="text-gray-500">분석 이미지를 불러오는 중...</span>
            )}
          </div>
        </div>
      </div>

      {/* 예측된 새 이름 */}
      {predictionText && (
        <div className="text-center text-2xl font-semibold text-blue-700 my-1 leading-tight h-[80px]">
          <div>🚨 <span className="font-bold underline">{predictionText}</span> 가 카메라에 나타났다!</div>
          <div>📢 {predictionText}가 싫어하는 소리로 쫓는 중...</div>
        </div>
      )}

      {/* 오디오 영역 */}
      <div className="grid grid-cols-2 gap-6">
        <div>
          <div className="text-center font-bold text-lg mb-3">최근에 녹음된 음성</div>
          <div className="border border-black h-36 flex items-center justify-center">
            {latestAudio ? (
              <audio controls>
                <source src={latestAudio} />
                브라우저가 오디오 태그를 지원하지 않습니다.
              </audio>
            ) : (
              <span className="text-gray-500">오디오를 불러오는 중...</span>
            )}
          </div>
        </div>
        <div>
          <div className="text-center font-bold text-lg mb-3">AI가 분석한 음성</div>
          <div className="border border-black h-36 flex items-center justify-center">
            {analyzedAudio ? (
              <audio controls>
                <source src={analyzedAudio} />
                브라우저가 오디오 태그를 지원하지 않습니다.
              </audio>
            ) : (
              <span className="text-gray-500">분석 오디오를 불러오는 중...</span>
            )}
          </div>
            {analyzedAudio && (
              <div className="text-center text-2xl font-semibold text-blue-700 my-1 leading-tight h-[80px]">
                <div>🚨 <span className="font-bold underline">{analyzedAudio}</span> 가 마이크에 나타났다!</div>
                <div>📢 {analyzedAudio}가 싫어하는 소리로 쫓는 중...</div>
              </div>
            )}
        </div>
      </div>
    </div>
  );
};

export default ImageSection;
