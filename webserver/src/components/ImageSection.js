// components/ImageAudioSection.js
import React, { useEffect, useState } from 'react';

const ImageSection = () => {
  const [latestImage, setLatestImage] = useState(null);

  useEffect(() => {
    fetch('/api/latest-image')
      .then(res => res.json())
      .then(data => setLatestImage(data.imageUrl))
      .catch(() => setLatestImage(null));
  }, []);

  return (
    <div className="p-8 grid grid-rows-2 gap-12">
      {/* 상단 이미지 영역 */}
      <div className="grid grid-cols-2 gap-6">
        <div>
          <div className="text-center font-bold text-lg mb-3">최근에 찍힌 사진</div>
          <div className="border border-black h-72 flex items-center justify-center">
            {latestImage ? (
              <img
                src={latestImage}
                alt="최근 이미지"
                className="h-full object-contain"
              />
            ) : (
              <span className="text-gray-500">이미지를 불러오는 중...</span>
            )}
          </div>
        </div>
        <div>
          <div className="text-center font-bold text-lg mb-3">AI가 분석한 사진</div>
          <div className="border border-black h-72 flex items-center justify-center">
            이미지 표시 영역
          </div>
        </div>
      </div>

      {/* 하단 오디오 영역 */}
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
