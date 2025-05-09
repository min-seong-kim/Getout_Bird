import React, { useEffect, useState } from 'react';

const ImageSection = () => {
  const [latestImage, setLatestImage] = useState(null);
  const [analyzedImage, setAnalyzedImage] = useState(null);

  useEffect(() => {
    fetch('http://220.149.235.221:4000/api/images')
      .then(res => res.json())
      .then(fileList => {
        const sorted = fileList
          .filter(name => name.startsWith('frame_') && name.endsWith('.jpg'))
          .sort((a, b) => {
            const getTime = f => {
              const match = f.match(/frame_(\d+)\.jpg/);
              return match ? parseInt(match[1]) : 0;
            };
            return getTime(b) - getTime(a);
          });

        if (sorted.length > 0) {
          setLatestImage(`http://220.149.235.221:4000/images/${sorted[0]}`);
        } else {
          setLatestImage(null);
        }
      })
      .catch(err => {
        console.error("이미지 불러오기 실패:", err);
        setLatestImage(null);
      });
    fetch('http://220.149.235.221:4000/api/images_result')
      .then(res => res.json())
      .then(fileList => {
        const sorted = fileList
          .filter(name => name.endsWith('.jpg'))
          .sort((a, b) => {
            const getTime = f => {
              const match = f.match(/frame_(\d+)\.jpg/);
              return match ? parseInt(match[1]) : 0;
            };
            return getTime(b) - getTime(a);
          });

        if (sorted.length > 0) {
          setAnalyzedImage(`http://220.149.235.221:4000/images_result/${sorted[0]}`);
        } else {
          setAnalyzedImage(null);
        }
      })
      .catch(err => {
        console.error("❌ 분석 이미지 불러오기 실패:", err);
        setAnalyzedImage(null);
      });
  }, []);

  return (
    <div className="p-8 grid grid-rows-2 gap-12">
      <div className="grid grid-cols-2 gap-6">
        <div>
          <div className="text-center font-bold text-lg mb-3">최근에 찍힌 사진</div>
          <div className="border border-black h-72 flex items-center justify-center">
            {latestImage ? (
              <img
                src={latestImage}
                alt="최근 이미지"
                className="max-h-full object-contain"
                onError={() => console.log("❌ 이미지 로딩 실패:", latestImage)}
              />
            ) : (
              <span className="text-gray-500">이미지를 불러오는 중...</span>
            )}
          </div>
        </div>
        <div>
          <div className="text-center font-bold text-lg mb-3">AI가 분석한 사진</div>
          <div className="border border-black h-72 flex items-center justify-center">
            {analyzedImage ? (
              <img
                src={analyzedImage}
                alt="AI 분석 이미지"
                className="max-h-full object-contain"
              />
            ) : (
              <span className="text-gray-500">분석 이미지를 불러오는 중...</span>
            )}
          </div>
        </div>
      </div>

      <div className="grid grid-cols-2 gap-6">
        <div>
          <div className="text-center font-bold text-lg mb-3">최근에 녹음된 음성</div>
          <div className="border border-black h-36 flex items-center justify-center text-sm">
            오디오 표시 영역
          </div>
        </div>
        <div>
          <div className="text-center font-bold text-lg mb-3">AI가 분석한 음성</div>
          <div className="border border-black h-36 flex items-center justify-center text-sm">
            오디오 표시 영역
          </div>
        </div>
      </div>
    </div>
  );
};

export default ImageSection;