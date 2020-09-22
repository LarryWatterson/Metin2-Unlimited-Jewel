// find

SetSocket(2, time);

// change
#ifdef LWT_UNLIMITED_JEWEL
	if (GetSocket(3) < 1)
		SetSocket(2, time);
#else
	SetSocket(2, time);
#endif
// find

void CItem::StartAccessorySocketExpireEvent()
{
	if (!IsAccessoryForSocket())
		return;

// add under
#ifdef LWT_UNLIMITED_JEWEL
	if (GetSocket(3) >= 1)
		return
#endif